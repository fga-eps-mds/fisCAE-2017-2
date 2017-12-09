from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.forms import ModelForm
from django import forms
from user.models import Advisor, President, Administrator, Person
from django.contrib.auth.models import User
from django.forms.widgets import TextInput


class AdvisorForm(ModelForm):
    name = forms.CharField(label='Nome', max_length=50)
    cpf = forms.CharField(label='CPF', max_length=12)
    municipio = forms.CharField(label='Município', max_length=30)
    bairro = forms.CharField(label='Bairro', max_length=30)
    uf = forms.CharField(label='UF', max_length=2)
    cep = forms.CharField(label='CEP', max_length=10)

    class Meta:
        model = Advisor
        exclude = ['user', 'nome_cae', 'tipo_cae']

    def __init__(self, *args, **kwargs):
        super(AdvisorForm, self).__init__(*args, **kwargs)
        self.fields['cep'].widget = TextInput(attrs={
            'id': 'cep',
            'class': 'cep',
            'name': 'cep',
            'placeholder': '',
            'onblur': 'pesquisacep(this.value)'
            })
        self.fields['bairro'].widget = TextInput(attrs={
            'id': 'bairro',
            'class': 'bairro',
            'name': 'bairro',
            'placeholder': '',
            })
        self.fields['municipio'].widget = TextInput(attrs={
            'id': 'municipio',
            'class': 'municipio',
            'name': 'municipio',
            'placeholder': '',
            })
        self.fields['uf'].widget = TextInput(attrs={
            'id': 'uf',
            'class': 'uf',
            'name': 'uf',
            'placeholder': '',
            })


class PresidentForm(ModelForm):
    name = forms.CharField(label="Nome", max_length=50)
    email = forms.EmailField(label="Email", max_length=100)
    username = forms.CharField(label="Usuário", max_length=50)
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(),
        max_length=32
        )

    class Meta:
        model = President
        exclude = [
            'user',
            'cpf',
            'cep',
            'bairro',
            'municipio',
            'uf',
            'tipo_cae',
            'nome_cae'
            ]

    def save(self, commit=True):
        president = super(PresidentForm, self).save(commit=False)
        president.name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        president.email = email
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Este nome de usuário já está cadastrado!')
        elif Person.objects.filter(email=email).exists():
            self.add_error('email', 'Este email já está cadastrado!')
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            president.user = user
            content_type = ContentType.objects.get_for_model(President)
            president_perm = Permission.objects.get(codename='president',
                                                    content_type=content_type)
            user.user_permissions.add(president_perm)
            if commit:
                president.save()
                return president


class AdministratorForm(ModelForm):
    name = forms.CharField(label="Nome", max_length=50)
    email = forms.EmailField(label="Email", max_length=100)
    username = forms.CharField(label="Usuário", max_length=50)
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(),
        max_length=32
        )

    class Meta:
        model = Administrator
        exclude = ["user"]

    def save(self, commit=True):
        admin = super(AdministratorForm, self).save(commit=False)
        admin.name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        admin.email = email
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Este usuário já está cadastrado!')
        elif Person.objects.filter(email=email).exists():
            self.add_error('email', 'Este email já está cadastrado!')
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            is_superuser=True)
            admin.user = user
            content_type = ContentType.objects.get_for_model(Administrator)
            admin_perm = Permission.objects.get(codename='administrator',
                                                content_type=content_type)
            user.user_permissions.add(admin_perm)
            if commit:
                admin.save()
                return admin


class ConfirmUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConfirmUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['is_active'].help_text = None
        self.fields['email'].help_text = None
        self.fields['email'].widget.attrs['readonly'] = True

    class Meta:
        model = User
        fields = ('username', 'email', 'is_active',)

    def save(self, commit=True):
        user = super(ConfirmUserForm, self)
        if commit:
            user.save()

        return user
