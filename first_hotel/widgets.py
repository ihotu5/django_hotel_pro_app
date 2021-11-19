from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe






class ShowHidePasswordWidget(forms.PasswordInput):
    class Media:
        js = ('script.js',)

    def render(self, name, value, attrs=None, **kwargs):
        final_attrs = self.build_attrs(attrs)
        output = self.get_template(final_attrs,value)
        return mark_safe(output)

    def get_template(self, attrs, value):
        flat_attrs = flatatt(attrs)
        return (
            
                    '''
                          <input %(attrs)s name="password" type="password" value="%(value)s"/>
                          <span id="__action__%(id)s__show_button">
                             <a href="javascript:show_pwd()">Show</a></span>
                          <span id="__action__%(id)s__hide_button" style="display:none;">
                             <a href="javascript:hide_pwd()">Hide</a></span>
                     '''                 
                ) % {
                    'attrs': flat_attrs,
                    'id': attrs['id'],
                    'value': value,
            
                }
