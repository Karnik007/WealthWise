from django import forms
from .models import User, Income, Expense, Bill

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class IncomeForm(forms.ModelForm):
    INCOME_CATEGORIES = [
        ('salary', '💰'),
        ('business', '💼'),
        ('freelance', '💻'),
        ('investments', '📈'),
        ('rental', '🏠'),
        ('other', '🎁')
    ]
    
    source = forms.ChoiceField(choices=INCOME_CATEGORIES, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter amount'
    }))
    
    class Meta:
        model = Income
        fields = ['source', 'amount']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.emoji = self.cleaned_data['source'].split()[0]
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

class ExpenseForm(forms.ModelForm):
    EXPENSE_CATEGORIES = [
        ('food', '🍕'),
        ('transportation', '🚗'),
        ('utilities', '💡'),
        ('rent', '🏠 Rent'),
        ('shopping', '🛍️'),
        ('entertainment', '🎬'),
        ('healthcare', '⚕️'),
        ('education', '📚'),
        ('other', '📦')
    ]
    
    category = forms.ChoiceField(choices=EXPENSE_CATEGORIES, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter amount'
    }))
    class Meta:
        model = Expense
        fields = ['category', 'amount']

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        instance.emoji = self.cleaned_data['category'].split()[0]
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

class billForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['bill_name', 'amount', 'due_date']