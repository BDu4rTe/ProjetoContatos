from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User


def login(request):
    return render(request, 'contas/login.html')


def logout(request):
    return render(request, 'contas/logout.html')


def register(request):
    if request.method != 'POST':
        return render(request, 'contas/register.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    rep_senha = request.POST.get('rep_senha')

    if not nome or not sobrenome or not email or not usuario or not senha \
            or not rep_senha:
        messages.error(request, 'Todos os campos devem ser preenchidos')
        return render(request, 'contas/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email invalido')
        return render(request, 'contas/register.html')

    if len(senha) < 6:
        messages.error(request, 'Senha deve ter pelo menos 6 caracteres')
        return render(request, 'contas/register.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuario deve ter pelo menos 6 caracteres')
        return render(request, 'contas/register.html')

    if senha != rep_senha:
        messages.error(request, 'Senhas nao sao iguais, digite novamente')
        return render(request, 'contas/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario ja existente')
        return render(request, 'contas/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email ja existente')
        return render(request, 'contas/register.html')

    messages.success(request, 'Registrado com sucesso!!')

    user = User.objects.create_user(
        username=usuario, email=email,
        password=senha, first_name=nome,
        last_name=sobrenome
    )
    user.save()
    return redirect('login')


def adm(request):
    return render(request, 'contas/adm.html')
