from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("contact", views.contact, name='contact'),
    path("dashboard",views.dashboard, name='dashboard'),
    path("dashboarddata",views.dashboarddata, name='dashboarddata'),
   # path("forgot-password",views.forgotpassword, name='forgot-password'),
    path("logout",views.logout, name='logout'),

    path("addunit",views.addunit, name='addunit'),
    path("products", views.products, name='products'),
    path('productdetails',views.productdetails, name="productdetails"),

    path("dealers",views.dealers, name="dealers"),
    path("adddealer", views.adddealer, name="adddealer"),

    path("vendors", views.vendors, name="vendors"),
    path("addvendor", views.addvendor, name="addvendor"),
    path("company",views.company, name="company"),

    path('<int:id>/', views.addunit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete"),

    path('editvendor/<int:id>/',views.addvendor, name="editvendor"),
    path('deletevendor/<int:id>/',views.deletevendor, name="deletevendor"),

    path('editdealer/<int:id>/',views.adddealer, name="editdealer"),
    path('deletedealer/<int:id>/',views.deletedealer, name="deletedealer"),

    path('editcompany/<int:id>/',views.editcompany, name="editcompany"),

    path("forgot-password",auth_views.PasswordResetView.as_view(template_name = 'forgot-password.html'), name="forgot_password"),
    path("reset_password_sent",auth_views.PasswordResetDoneView.as_view(template_name = 'reset_password/password_reset_done.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete",auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('sales',views.sales, name="sales"),
    path('addsell', views.addsell, name="addsell"),
    path('editsell/<int:id>/',views.addsell, name="editsales"),
    path('deletesell/<int:id>/',views.deletesell, name="deletesales"),

    path('buy',views.buy, name="buy"),
    path('addbuy', views.addbuy, name="addbuy"),
    path('editbuy/<int:id>/',views.addbuy, name="editbuy"),
    path('deletebuy/<int:id>/',views.deletebuy, name="deletebuy"),

    path('warehouse',views.warehouse, name="warehouse"),
    path('addwarehouse', views.addwarehouse, name="addwarehouse"),
    path('editwarehouse/<int:id>/',views.addwarehouse, name="editwarehouse"),
    path('deletewarehouse/<int:id>/',views.deletewarehouse, name="deletewarehouse"),

    path('bank',views.bank, name="bank"),
    path('addbank', views.addbank, name="addbank"),
    path('editbank/<int:id>/',views.addbank, name="editbank"),
    path('deletebank/<int:id>/',views.deletebank, name="deletebank"),

    path('changepassword', views.changepassword, name="changepassword"),

    path('settings', views.settings, name="settings"),
    path('reports', views.reports, name="reports"),

    path("about", views.about, name="about")
    
]