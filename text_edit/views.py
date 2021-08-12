from django.views.generic.edit import FormView

from . import forms


class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"
    
     # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        a = data["a"]
        b = data["b"]
        c = data["c"]
        d = data["d"]
        e = data["e"]
        f = data["f"]
        g = data["g"]
        h = data["h"]
        i = data["i"]
        j = data["j"]
        k = data["k"]
        l = data["l"]
        m = data["m"]
        n = data["n"]
        o = data["o"]
        
        new_text = (a*10000+b*5000+c*1000+d*500+e*100+f*50+g*10+
                    h*5+i+j*25000+k*5000+l*2500+m*500+n*250+o*50)
        
        # テンプレートに渡す
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)
