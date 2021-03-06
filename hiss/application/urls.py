from django.urls import path

from application import views

app_name = "application"
urlpatterns = [
    path("", views.CreateApplicationView.as_view(), name="create"),
    path("<uuid:pk>", views.UpdateApplicationView.as_view(), name="update"),
    path("<uuid:pk>/confirm", views.ConfirmApplicationView.as_view(), name="confirm"),
    path("<uuid:pk>/decline", views.DeclineApplicationView.as_view(), name="decline"),
    path("all", views.GetApplicationsCsvView.as_view(), name="get_all_applications"),
    path("all/json", views.GetApplicationsJsonView.as_view(), name="get_all_applications_json"),
]
