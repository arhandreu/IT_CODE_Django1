from django import forms
from homew import models


class AddClientForm(forms.Form):
    firstname = forms.CharField(max_length=255, label="Имя")
    lastname = forms.CharField(max_length=255, label="Фамилия")
    credit_number = forms.IntegerField(label="Номер кредитной карты")
    privilege = forms.ChoiceField(choices=models.Client.PRIVILEGE,
                                  label="Статус клиента",
                                  )
