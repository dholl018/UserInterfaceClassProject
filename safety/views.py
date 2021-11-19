from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from actions.models import Action
from .models import regular_user, admin_user, SafetyReport, CommentSection
from django.http import JsonResponse


# Create your views here.
def safety_report_list(request):
    report = SafetyReport.objects.all()
    return render(request,
                  "Safety/safety_report/list.html",
                  {"reports": report}
                  )


def search_results(request):
    report = SafetyReport.objects.all()
    if 'role' not in request.session:
        return redirect('Safety:home')
    return render(request,
                  "Safety/safety_report/searchresults.html",
                  )


def safety_report_detail(request, report_id):
    report = SafetyReport.objects.get(id=report_id)
    return render(request,
                  "Safety/safety_report/details.html",
                  {'report': report}
                  )


def edit_report(request, report_id):
    if 'role' not in request.session:
        return redirect('Safety:home')
    report = SafetyReport.objects.get(id=report_id)
    # if 'role' not in request.session:
    #    return redirect('Safety:home')
    #    key = request.GET.get(report_id)
    #    for report in new_report:
    #        if key == report.id:
    #            break
    return render(request,
                  "Safety/safety_report/edit.html",
                  {'report': report}
                  )


def edit_report_submit(request, report_id):
    if 'role' not in request.session:
        return redirect('Safety:home')
    report = SafetyReport.objects.get(id=report_id)
    if request.method == 'POST':
        author = request.session.get("username")
        date = request.POST.get("updated_date")
        description = request.POST.get("updated_report")
        location = request.POST.get("location")
        title = request.POST.get("title")
        user = User.objects.get(username=request.session.get("username"))
        report = SafetyReport(
            title=title,
            description=description,
            date_posted=date,
            location=location,
            author=author,
            user=user,
        )
        report.save()
        # Redirect to detail view
        action = Action(
            user=user,
            verb="Edited a Report",
            target=report,
        )
        messages.add_message(request, messages.INFO, "Report titled: %s has been edited" % report.title)
        return render(request,
                      "Safety/safety_report/details.html",
                      {'report': report}
                      )
    else:
        return render(request,
                      "Safety/safety_report/list.html",
                      {"reports": report}
                      )


def delete_report(request, report_id):
    if 'role' not in request.session:
        return redirect('Safety:home')
    user = User.objects.get(username=request.session.get("username"))
    report = SafetyReport.objects.get(id=report_id)
    messages.add_message(request, messages.WARNING, "Report titled: %s has been DELETED" % report.title)
    # delete Report
    action = Action(
        user=user,
        verb="Deleted a report",
        target=report,
    )
    action.save()
    report.delete()
    return redirect('Safety:safety_report_list')


def home(request):
    return render(request,
                  "Safety/home.html",
                  )


def about(request):
    return render(request,
                  "Safety/about.html",
                  )


def privacy(request):
    return render(request,
                  "Safety/privacy.html",
                  )


def add_report(request):
    if 'role' not in request.session:
        return redirect('Safety:home')
    if request.method == 'POST':
        author = request.session.get("username")
        date = request.POST.get("date")
        description = request.POST.get("report")
        location = request.POST.get("location")
        title = request.POST.get("title")
        user = User.objects.get(username=request.session.get("username"))
        sr = SafetyReport(
            title=title,
            description=description,
            date_posted=date,
            location=location,
            author=author,
            user=user,
        )
        sr.save()
        # log new report
        action = Action(
            user=user,
            verb="Created a new Report.",
            target=sr,
        )
        action.save()
        messages.add_message(request, messages.SUCCESS, "You have successfully added item: %s" % sr.title)
        # Redirect to detail view
        return render(request,
                      "Safety/safety_report/details.html",
                      {'report': sr}
                      )
    else:
        return render(request,
                      "Safety/safety_report/Add_Item.html",
                      )


def new_safety_report(request):
    if 'username' not in request.session:
        return redirect('Safety:home')
    return render(request,
                  "Safety/safety_report/Add_Item.html",
                  )


def home_user_logged_in(request):
    if 'username' not in request.session:
        actions = Action.objects.all()[0:10]
    else:
        username = request.session['username']
        user1 = get_object_or_404(User, username=username)
        actions = Action.objects.filter(user=user1)
    return render(request,
                  "Safety/home_user_Logged_In.html",
                  {"actions": actions}
                  )


def my_safety_reports(request):
    if 'role' not in request.session:
        return redirect('Safety:home')
    return render(request,
                  "Safety/safety_report/MyReports.html",
                  )




def locked_post(request):
    if 'role' not in request.session:
        return redirect('Safety:home')
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        report_id = request.POST.get('report_id')
        try:
            report = SafetyReport.objects.get(pk=report_id)
            report.mod_Locked = not report.mod_Locked
            report.save()
            return JsonResponse({'success': 'success', 'mod_locked': report.mod_Locked}, status=200)
        except SafetyReport.DoesNotExist:
            return JsonResponse({'error': 'no report found'}, status=200)
    else:
        return JsonResponse({'error': 'invalid Ajax request'}, status=400)


def like_post(request):
    if 'role' not in request.session:
        return redirect('Safety:home')
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        report_id = request.POST.get('report_id')
        report = SafetyReport.objects.get(pk=report_id)
        try:
            report = SafetyReport.objects.get(pk=report_id)
            report.like = report.like + 1
            report.save()
        except SafetyReport.DoesNotExist:
            return JsonResponse({'error': 'no report found'}, status=200)
    else:
        return JsonResponse({'error': 'invalid Ajax request'}, status=400)


def reorder_list(request):
    if 'role' not in request.session:
        return redirect('Safety:home')
    report = SafetyReport.objects.all().order_by('title')
#    report.save()
    return render(request,
                  "Safety/safety_report/list.html",
                  {"reports": report}
                  )


def post_comment(request, report_id):
    if request.method == "POST":
        report = SafetyReport.objects.get(pk=report_id)
        author = request.session.get("username")
        new_comment = request.POST.get('newComment')
        linked_report = report_id
        user = User.objects.get(username=request.session.get("username"))
        cs = CommentSection(
            author=author,
            comment=new_comment,
            attached_report=linked_report,
            report_id=linked_report,
        )
        cs.save()
        # posted a comment
        action = Action(
            user=user,
            verb="Commented on a post",
            target=cs,
        )
        action.save()
        return render(request,
                      "Safety/safety_report/details.html",
                      {'report': report}
                      )


def edit_comment(request, report_id, comment_id):
    if request.method == "POST":
        report = SafetyReport.objects.get(pk=report_id)
        comment = CommentSection.objects.get(pk=comment_id)
        new_comment = request.POST.get('editComment')
        comment.comment = new_comment
        comment.save()
        return render(request,
                      "Safety/safety_report/details.html",
                      {'report': report}
                      )


def delete_comment(request, report_id, comment_id):
    if request.method == "POST":
        report = SafetyReport.objects.get(pk=report_id)
        comment = CommentSection.objects.get(pk=comment_id)
        comment.delete()
        return render(request,
                      "Safety/safety_report/details.html",
                      {'report': report}
                      )