#coding = utf-8
__author__ = 'jun'
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

'''
�ܶ��˾����������ø��鷳����ʵ��Ȼ����Ϊ Django �� forms �ṩ�˺��õļ������ܣ�

ģ���б�����Ⱦ��
���ݵ���֤������ĳһЩ���벻�Ϸ�Ҳ���ᶪʧ�Ѿ���������ݣ�
�����Զ��Ƹ����ӵ���֤����������ṩ�� 10 ������򣬱���Ҫ���������������ϵȹ��ܣ��� forms.py ��ʵ�ֶ��Ǻ����׵ġ�
����Ҳ��һЩ�� Django forms ��Ⱦ�� Bootstrap �Ĳ����ʹ������ʮ�ַ��㡣
'''