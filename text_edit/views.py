from django.views.generic.edit import FormView

from . import forms


def prime_count(number):
    number = int(number)
    if number < 2:
        return str(number) + "です。"
    elif number == 2:
        return str(number) + "は素数です。"
    prime_num_list = []
    while number != 1:
        if number%2 == 0:
            number = number//2
            prime_num_list.append(2)
            continue
        for count in range(3, int(number**0.5) + 1, 2):
            if number % count == 0:
                prime_num_list.append(count)
                number = number//count
                break
        else:
            prime_num_list.append(number)
            number = 1
    if len(prime_num_list) == 1:
        return str(prime_num_list[0]) + "は素数"
    prime_set = sorted(list(set(prime_num_list)))
    prime_set_list = []
    for set_num in prime_set:
        set_count = prime_num_list.count(set_num)
        if set_count != 1:
            prime_set_list.append(str(int(set_num)) + "の" + str(set_count) + "乗")
        else:
            prime_set_list.append(str(int(set_num)))
    prime_num = str(prime_set_list).replace(',', '×').translate(
                str.maketrans({"'": None, "[": None, "]": None}))
    return prime_num

class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"

     # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        number = form.cleaned_data["number"]
        # テンプレートに渡す
        import time
        start = time.time()
        prime_number = prime_count(number)
        calculation_time = time.time() - start
        ctxt = self.get_context_data(prime_number=prime_number,
                                    calculation_time=calculation_time,
                                    form=form, number=number)
        return self.render_to_response(ctxt)
