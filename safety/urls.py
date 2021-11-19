from django.urls import path
from . import views
app_name = 'Safety'
urlpatterns = [
    # safety_report views
    path('', views.home, name='home'),
    path('privacy', views.privacy, name='privacy'),
    path('about', views.about, name='about'),
    path('home', views.home_user_logged_in, name='home_user_logged_in'),
    path('list', views.safety_report_list, name='safety_report_list'),
    path('list/order', views.reorder_list, name='reorder_list'),
    path('list/locked', views.locked_post, name='locked-post'),
    path('list/like_post', views.like_post, name='like-post'),
    path('list/myreports', views.my_safety_reports, name='my_safety_reports'),
    path('list/newreport', views.new_safety_report, name='new_safety_report'),
    path('list/addreport', views.add_report, name='add_report'),
    path('list/<int:report_id>', views.safety_report_detail, name='report-details'),
    path('list/<int:report_id>/comment', views.post_comment, name='post-comment'),
    path('list/<int:report_id>/<int:comment_id>', views.edit_comment, name='edit-comment'),
    path('list/<int:report_id>/<int:comment_id>/delete', views.delete_comment, name='delete-comment'),
    path('list/edit/<int:report_id>', views.edit_report, name='edit_report'),
    path('list/edit/<int:report_id>/submit', views.edit_report_submit, name='edit_report_submit'),
    path('list/edit/<int:report_id>/delete', views.delete_report, name='delete_report'),
    path('list/search', views.search_results, name='search_results'),
]