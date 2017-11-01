from django.conf.urls import url
from cmoapp.views import OperatorManager, ApiManager

urlpatterns = [
    url(r'^$', OperatorManager.index, name="Operator_Index"),
    url(r'^(?P<pk>\d+)', OperatorManager.assignnewCrisis, name='Operator_AssignCrisis'),
    url(r'^create_crisis/$', OperatorManager.create_crisis, name="create_crisis"),
    url(r'^delete_crisis/$', OperatorManager.delete_crisis, name="delete_crisis"),
    url(r'^load_crisis/$', OperatorManager.load_crisis, name="load_crisis"),
    url(r'^assignexisting/$', OperatorManager.assignexisting, name="assignexisting"),

    url(r'^crisisdisplay/$', OperatorManager.getallassignedCrisisReport, name='getAssignedCrisis'),

    url(r'^load_analyst/$', OperatorManager.load_analyst, name="load_analyst"),

    url(r'^/crisisreports/$', OperatorManager.get_crisisreport_collection, name='Operator_Crisisreport'),


]