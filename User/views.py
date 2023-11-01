from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


# Create your views here.
def index(request):
    if not request.session.get('is_login', None):
        return render(request, 'User/login.html', locals())
    return render(request, 'User/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return render(request, 'User/index.html', locals())
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.OrdinaryUser.objects.get(user_name=username)
            except:
                message = '用户不存在！'
                return render(request, 'User/login.html', locals())

            if user.user_password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.user_id
                request.session['user_name'] = user.user_name
                return render(request, 'User/index.html', locals())
            else:
                message = '密码不正确！'
                return render(request, 'User/login.html', locals())
        else:
            return render(request, 'User/login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'User/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('User/index.html')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'User/register.html', locals())
            else:
                same_name_user = models.OrdinaryUser.objects.filter(user_name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'User/register.html', locals())
                same_email_user = models.OrdinaryUser.objects.filter(user_email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'User/register.html', locals())

                new_user = models.OrdinaryUser()
                new_user.user_name = username
                new_user.user_password = password1
                new_user.user_email = email
                new_user.accountStatus = 1
                new_user.save()
                message = '创建成功,请用账号登录！'
                return render(request, 'User/login.html', locals())
        else:
            return render(request, 'User/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'User/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return render(request, 'User/login.html', locals())
    register_form = forms.RegisterForm(request.POST)
    request.session.flush()
    # del request.session['is_login']
    register_form = forms.RegisterForm()
    return redirect("/User/login/")


def adminLogin(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return render(request, 'User/admin_index.html', locals())
    if request.method == 'POST':
        login_form = forms.AdminForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            admin_name = login_form.cleaned_data.get('admin_name')
            password = login_form.cleaned_data.get('password')
            try:
                admin = models.Administrator.objects.get(admin_name=admin_name)
            except:
                message = '用户不存在！'
                return render(request, 'User/adminLogin.html', locals())

            if admin.admin_password == password:
                request.session['is_login'] = True
                request.session['admin_id'] = admin.admin_id
                request.session['admin_name'] = admin.admin_name
                return render(request, 'User/admin_index.html', locals())
            else:
                message = '密码不正确！'
                return render(request, 'User/adminLogin.html', locals())
        else:
            return render(request, 'User/adminLogin.html', locals())
    login_form = forms.AdminForm()
    return render(request, 'User/adminLogin.html', locals())


def adminRegister(request):
    if request.session.get('is_login', None):
        return redirect('User/admin_index.html')
    if request.method == 'POST':
        register_form = forms.AdminRegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            admin_name = register_form.cleaned_data.get('admin_name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'User/adminRegister.html', locals())
            else:
                same_name_admin = models.Administrator.objects.filter(admin_name=admin_name)
                if same_name_admin:
                    message = '用户名已经存在'
                    return render(request, 'User/adminRegister.html', locals())
                same_email_admin = models.Administrator.objects.filter(admin_email=email)
                if same_email_admin:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'User/adminRegister.html', locals())

                new_admin = models.Administrator()
                new_admin.admin_name = admin_name
                new_admin.admin_password = password1
                new_admin.admin_email = email
                new_admin.save()
                message = '创建成功,请用账号登录！'
                return render(request, 'User/adminLogin.html', locals())
        else:
            return render(request, 'User/adminRegister.html', locals())
    register_form = forms.AdminRegisterForm()
    return render(request, 'User/adminRegister.html', locals())
