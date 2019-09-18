from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from .models import RegionModel
from .models import SERVICE_CHOICES, REGION_CHOICES
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class SE_Form(forms.ModelForm):

    ###################################### first card #################################################

    residential_premises_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    residential_premises_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    residential_premises_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    residential_premises_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk1'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea1','rows':'2'}),
                        label='',required=False)
    residential_premises_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk2'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea2','rows':'2'}),
                        label='',required=False)
    residential_premises_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk3'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea3','rows':'2'}),
                        label='',required=False)
    residential_premises_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk4'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea4','rows':'2'}),
                        label='',required=False)
    residential_premises_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk5'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea5','rows':'2'}),
                        label='',required=False)
    residential_premises_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk6'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea6','rows':'2'}),
                        label='',required=False)
    residential_premises_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk7'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea7','rows':'2'}),
                        label='',required=False)
    residential_premises_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk8'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea8','rows':'2'}),
                        label='',required=False)
    residential_premises_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk9'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea9','rows':'2'}),
                        label='',required=False)
    residential_premises_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk10'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea10','rows':'2'}),
                        label='',required=False)
    residential_premises_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk11'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea11','rows':'2'}),
                        label='',required=False)
    residential_premises_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk12'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    residential_premises_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea12','rows':'2'}),
                        label='',required=False)

    ###################################### second card #################################################

    housing_transfer_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    housing_transfer_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    housing_transfer_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    housing_transfer_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk13'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea13', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk14'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea14', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk15'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea15', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk16'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea16', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk17'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea17', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk18'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea18', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk19'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea19', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk20'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea20', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk21'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea21', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk22'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea22', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk23'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea23', 'rows': '2'}),
                        label='', required=False)
    housing_transfer_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk24'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    housing_transfer_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea24', 'rows': '2'}),
                        label='', required=False)

    ###################################### third card #################################################

    advertising_structures_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    advertising_structures_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    advertising_structures_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    advertising_structures_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk25'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea25', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk26'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea26', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk27'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea27', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk28'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea28', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk29'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea29', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk30'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea30', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk31'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea31', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk32'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea32', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk33'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea33', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk34'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea34', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk35'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea35', 'rows': '2'}),
                        label='', required=False)
    advertising_structures_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk36'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    advertising_structures_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea36', 'rows': '2'}),
                        label='', required=False)

    ###################################### fourth card #################################################

    capital_construction_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    capital_construction_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    capital_construction_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    capital_construction_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk37'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea37', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk38'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea38', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk39'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea39', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk40'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea40', 'rows': '2'}),
                        label='', required=False)
    capital_construction_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk41'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea41', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk42'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea42', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk43'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea43', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk44'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea44', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk45'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea45', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk46'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea46', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk47'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea47', 'rows': '2'}),
                        label='', required=False)
    capital_construction_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk48'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    capital_construction_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea48', 'rows': '2'}),
                        label='', required=False)

    ###################################### fifth card #################################################

    preschool_education_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    preschool_education_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    preschool_education_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    preschool_education_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk49'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea49', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk50'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea50', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk51'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea51', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk52'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea52', 'rows': '2'}),
                        label='', required=False)
    preschool_education_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk53'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea53', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk54'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea54', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk55'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea55', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk56'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea56', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk57'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea57', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk58'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea58', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk59'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea59', 'rows': '2'}),
                        label='', required=False)
    preschool_education_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk60'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    preschool_education_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea60', 'rows': '2'}),
                        label='', required=False)

    ###################################### sixth card #################################################

    school_education_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    school_education_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    school_education_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    school_education_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk61'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea61', 'rows': '2'}),
                        label='', required=False)
    school_education_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk62'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea62', 'rows': '2'}),
                        label='', required=False)
    school_education_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk63'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea63', 'rows': '2'}),
                        label='', required=False)
    school_education_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk64'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea64', 'rows': '2'}),
                        label='', required=False)
    school_education_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk65'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea65', 'rows': '2'}),
                        label='', required=False)
    school_education_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk66'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea66', 'rows': '2'}),
                        label='', required=False)
    school_education_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk67'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea67', 'rows': '2'}),
                        label='', required=False)
    school_education_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk68'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea68', 'rows': '2'}),
                        label='', required=False)
    school_education_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk69'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea69', 'rows': '2'}),
                        label='', required=False)
    school_education_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk70'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea70', 'rows': '2'}),
                        label='', required=False)
    school_education_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk71'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea71', 'rows': '2'}),
                        label='', required=False)
    school_education_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk72'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    school_education_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea72', 'rows': '2'}),
                        label='', required=False)

    ###################################### seventh card #################################################

    needing_premises_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    needing_premises_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    needing_premises_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    needing_premises_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk73'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea73', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk74'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea74', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk75'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea75', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk76'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea76', 'rows': '2'}),
                        label='', required=False)
    needing_premises_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk77'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea77', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk78'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea78', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk79'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea79', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk80'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea80', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk81'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea81', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk82'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea82', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk83'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea83', 'rows': '2'}),
                        label='', required=False)
    needing_premises_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk84'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    needing_premises_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea84', 'rows': '2'}),
                        label='', required=False)

    ###################################### eighth card #################################################

    town_planning_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    town_planning_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    town_planning_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    town_planning_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk85'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea85', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk86'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea86', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk87'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea87', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk88'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea88', 'rows': '2'}),
                        label='', required=False)
    town_planning_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk89'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea89', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk90'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea90', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk91'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea91', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk92'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea92', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk93'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea93', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk94'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea94', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk95'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea95', 'rows': '2'}),
                        label='', required=False)
    town_planning_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk96'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    town_planning_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea96', 'rows': '2'}),
                        label='', required=False)

    ###################################### nineth card #################################################

    archive_reference_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    archive_reference_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    archive_reference_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    archive_reference_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk97'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea97', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk98'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea98', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk99'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea99', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk100'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea100', 'rows': '2'}),
                        label='', required=False)
    archive_reference_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk101'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea101', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk102'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea102', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk103'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea103', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk104'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea104', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk105'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea105', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk106'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea106', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk107'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea107', 'rows': '2'}),
                        label='', required=False)
    archive_reference_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk108'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    archive_reference_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea108', 'rows': '2'}),
                        label='', required=False)

    ###################################### tenth card #################################################

    land_schemes_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    land_schemes_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_schemes_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_schemes_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk109'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea109', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk110'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea110', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk111'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea111', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk112'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea112', 'rows': '2'}),
                        label='', required=False)
    land_schemes_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk113'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea113', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk114'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea114', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk115'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea115', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk116'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea116', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk117'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea117', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk118'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea118', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk119'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea119', 'rows': '2'}),
                        label='', required=False)
    land_schemes_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk120'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_schemes_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea120', 'rows': '2'}),
                        label='', required=False)
    ###################################### eleventh card #################################################

    land_sale_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    land_sale_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_sale_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_sale_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk121'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea121', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk122'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea122', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk123'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea123', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk124'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea124', 'rows': '2'}),
                        label='', required=False)
    land_sale_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk125'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea125', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk126'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea126', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk127'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea127', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk128'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea128', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk129'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea129', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk130'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea130', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk131'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea131', 'rows': '2'}),
                        label='', required=False)
    land_sale_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk132'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_sale_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea132', 'rows': '2'}),
                        label='', required=False)

    ###################################### twelth card #################################################

    land_lease_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    land_lease_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_lease_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    land_lease_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk133'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea133', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk134'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea134', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk135'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea135', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk136'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea136', 'rows': '2'}),
                        label='', required=False)
    land_lease_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk137'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea137', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk138'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea138', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk139'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea139', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk140'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea140', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk141'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea141', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk142'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea142', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk143'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea143', 'rows': '2'}),
                        label='', required=False)
    land_lease_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk144'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    land_lease_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea144', 'rows': '2'}),
                        label='', required=False)
    ###################################### thirteenth card #################################################

    ownership_right_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    ownership_right_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    ownership_right_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    ownership_right_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk145'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea145', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk146'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea146', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk147'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea147', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk148'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea148', 'rows': '2'}),
                        label='', required=False)
    ownership_right_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk149'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea149', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk150'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea150', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk151'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea151', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk152'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea152', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk153'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea153', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk154'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea154', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk155'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea155', 'rows': '2'}),
                        label='', required=False)
    ownership_right_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk156'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    ownership_right_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea156', 'rows': '2'}),
                        label='', required=False)

    ###################################### fourteenth card #################################################

    municipal_property_lease_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    municipal_property_lease_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    municipal_property_lease_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    municipal_property_lease_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk157'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea157', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk158'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea158', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk159'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea159', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk160'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea160', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk161'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea161', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk162'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea162', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk163'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea163', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk164'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea164', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk165'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea165', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk166'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea166', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk167'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea167', 'rows': '2'}),
                        label='', required=False)
    municipal_property_lease_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk168'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    municipal_property_lease_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea168', 'rows': '2'}),
                        label='', required=False)
    ###################################### fifteenth card #################################################

    free_land_provision_id_rgmu = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=1000,required=False)
    free_land_provision_statement_amount = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    free_land_provision_link = \
        forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='', max_length=100, required=False)
    free_land_provision_has_advanced_appointment = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk169'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_advanced_appointment_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea169', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_btn_get_service = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk170'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_btn_get_service_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea170', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_reglament = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk171'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_reglament_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea171', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_estimation_quality = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk172'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_estimation_quality_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea172', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_connected_to_fgis_do = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk173'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_connected_to_fgis_do_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea173', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_electronic_form_printing = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk174'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_electronic_form_printing_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea174', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_edition_draft = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk175'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_edition_draft_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea175', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_term_of_consideration = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk176'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_term_of_consideration_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea176', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_notif_consider_result = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk177'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_notif_consider_result_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea177', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_causes_of_failure = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk178'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_causes_of_failure_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea178', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_sample_document = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk179'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_sample_document_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea179', 'rows': '2'}),
                        label='', required=False)
    free_land_provision_has_document_template = \
        forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input', 'id': 'chk180'}),
                          choices=SERVICE_CHOICES, label='', required=False)
    free_land_provision_has_document_template_comment = \
        forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'txtarea180', 'rows': '2'}),
                        label='', required=False)



    class Meta:
        model = RegionModel
        exclude = ('id', 'time', 'year', 'month', 'day', 'region_name')


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'password'}),max_length=100)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class PassResetForm(PasswordResetForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email',
                                                             'type':'email'}), max_length=100)


class PassResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                                 'placeholder':'Enter new password',
                                                                 'type':'password'}), max_length=100)
    new_password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Enter new password again',
                                                                 'type': 'password'}), max_length=100)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('region_name',)


class CustomUserChangeForm(UserChangeForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=254)

    class Meta:
        model = CustomUser
        fields = ('email','username')
