from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def tax_new_regime(taxable):
    tax = 0
    if taxable > 300000:
        slab = min(taxable,700000) - 300000
        if slab > 0: tax += slab * 0.05
    if taxable > 700000:
        slab = min(taxable,1000000) - 700000
        if slab > 0: tax += slab * 0.10
    if taxable > 1000000:
        tax += (taxable - 1000000) * 0.30
    cess = tax * 0.04
    return tax + cess

def tax_old_regime(taxable):
    tax = 0
    if taxable > 250000:
        slab = min(taxable,500000) - 250000
        if slab > 0: tax += slab * 0.05
    if taxable > 500000:
        slab = min(taxable,1000000) - 500000
        if slab > 0: tax += slab * 0.20
    if taxable > 1000000:
        tax += (taxable - 1000000) * 0.30
    cess = tax * 0.04
    return tax + cess

def estimate_inhand(ctc):
    basic = ctc * 0.40
    emp_pf = basic * 0.12
    ee_pf = basic * 0.12
    gross_salary = ctc - emp_pf - 40000
    taxable_income = gross_salary - ee_pf - 50000
    if taxable_income < 0: taxable_income = 0
    tax_new = tax_new_regime(taxable_income)
    tax_old = tax_old_regime(taxable_income)
    monthly_new = (gross_salary - ee_pf - tax_new) / 12
    monthly_old = (gross_salary - ee_pf - tax_old) / 12
    return monthly_new, monthly_old

class InHandApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text='Enter your CTC (₹ per year):', font_size=18)
        self.input = TextInput(hint_text='e.g. 1000000', multiline=False, input_filter='int')
        self.button = Button(text='Calculate', on_press=self.calculate)
        self.result = Label(text='', font_size=16)

        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(self.button)
        layout.add_widget(self.result)
        return layout

    def calculate(self, instance):
        try:
            ctc = int(self.input.text)
            new_inhand, old_inhand = estimate_inhand(ctc)
            self.result.text = (
                f'CTC: ₹{ctc:,}\n'
                f'In-Hand (New Regime): ₹{new_inhand:,.0f}/month\n'
                f'In-Hand (Old Regime): ₹{old_inhand:,.0f}/month'
            )
        except:
            self.result.text = 'Please enter a valid number.'

if __name__ == '__main__':
    InHandApp().run()
