from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .forms import SE_Form, LoginForm
from app.models import RegionModel

regions_names = ['Абзелиловский район РБ', 'Агидель РБ', 'Альшеевский район РБ', 'Архангельский район РБ',
                 'Аскинский район РБ', 'Аургазинский район РБ', 'Баймакский район РБ', 'Бакалинский район РБ',
                 'Балтачевский район РБ', 'Белебеевский район РБ', 'Белокатайский район РБ', 'Белорецкий район РБ',
                 'Бижбулякский район РБ', 'Бирский район РБ', 'Благоварский район РБ', 'Благовещенский район РБ',
                 'Буздякский район РБ', 'Бураевский район РБ', 'Бурзянский район РБ', 'Гафурийский район РБ',
                 'Давлекановский район РБ', 'Дуванский район РБ', 'Дюртюлинский район РБ', 'Ермекеевский район',
                 'Зианчуринский район РБ', 'Зилаирский район РБ', 'Иглинский район РБ', 'Илишевский район РБ',
                 'Ишимбайский район РБ', 'Калтасинский район РБ', 'Караидельский район РБ', 'Кармаскалинский район РБ',
                 'Кигинский район РБ', 'Краснокамский район РБ', 'Кугарчинский район РБ', 'Кумертау',
                 'Кушнаренковский район РБ', 'Куюргазинский район РБ', 'Межгорье', 'Мелеузовский район РБ',
                 'Мечетлинский район РБ', 'Мишкинский район РБ', 'Миякинский район РБ', 'Нефтекамск',
                 'Нуримановский район РБ', 'Октябрьский', 'Салават', 'Салаватский район РБ',
                 'Сибай', 'Стерлибашевский район РБ', 'Стерлитамак', 'Стерлитамакский район РБ',
                 'Татышлинский район РБ', 'Туймазинский район РБ', 'Уфа', 'Уфимский район РБ', 'Учалинский район РБ',
                 'Федоровский район РБ', 'Хайбуллинский район РБ', 'Чекмагушевский район РБ', 'Чишминский район РБ',
                 'Шаранский район РБ', 'Янаульский район РБ']

short_regions_names = ['abzelil', 'agidel', 'alsheev', 'archang', 'askinsk', 'aurgazin', 'baymak', 'bakalin', 'baltach',
                       'belebeev', 'belokatay', 'belorezk', 'bizhbul', 'birsk', 'blagovar', 'blagovesch', 'buzdyak',
                       'buraev', 'burzyan', 'gafur', 'davlekan', 'duvansk', 'dyurtyulin', 'ermekeev', 'zianchurin',
                       'zilairsk', 'iglinsk', 'ilishevsk', 'ishimbaysk', 'kaltasinsk', 'karaidelsks', 'karmaskalin',
                       'kiginsk', 'krasnokamsk', 'kugarchinsk', 'kumertau', 'kushnarenk', 'kuyurgazinsk', 'mezhgorie',
                       'meleuz', 'mechetlin', 'mishkin', 'miyakin', 'neftekamsk', 'nurimanovsk', 'oktabrsks',
                       'slavat', 'salavatskiy', 'sibi', 'sterlibash', 'sterlitamak', 'sterlitamakskiy',
                       'tatyshlin', 'tuymazin', 'ufa', 'ufimsk', 'uchalinsk', 'fedorovsk', 'haybullinsk',
                       'chekmagush', 'chishminsk', 'sharanck', 'yanaulsk']


class dotDict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


@login_required
def get_self_examination_form(request):
    """
    View function for renewing a specific regionForm by users
    """
    if request.user.is_authenticated :
        print(request.user.username)
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            region_form = SE_Form(request.POST)

            # Check if the form is valid:
            if region_form.is_valid():

                form_to_save = region_form.save(commit=False)
                form_to_save.time = datetime.today().time()
                form_to_save.day = datetime.today().strftime('%d')
                form_to_save.year = datetime.today().strftime('%Y')
                form_to_save.month = datetime.today().strftime('%m')
                form_to_save.save()

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('result_form', kwargs={
                    'service_name': 'residential_premises',
                    'year': datetime.today().strftime('%Y'),
                    'month': datetime.today().strftime('%m')
                }))

        # If this is a GET (or any other method) create the default form.
        else:
            region_form = SE_Form(initial={'region_name': 'Уфа',
                                       'residential_premises_id_RGMU': 'id_GRMU_redevelop1',
                                       'residential_premises_statement_amount': '555',
                                       'residential_premises_link': 'http:\\my_link_1.com',
                                       'housing_transfer_id_RGMU': 'id_GRMU_transfer1',
                                       'housing_transfer_statement_amount': '55566788',
                                       'housing_transfer_link': 'http:\\my_link_1234.com',
                                       'advertising_structures_id_RGMU': 'id_GRMU_advert1',
                                       'advertising_structures_statement_amount': '55566788',
                                       'advertising_structures_link': 'http:\\my_link_1234.com',
                                       'capital_construction_id_RGMU': 'id_GRMU_capital1',
                                       'capital_construction_statement_amount': '55566788',
                                       'capital_construction_link': 'http:\\my_link_1234.com',
                                       'preschool_education_id_RGMU': 'id_GRMU_preschool1',
                                       'preschool_education_statement_amount': '55566788',
                                       'preschool_education_link': 'http:\\my_link_1234.com',
                                       'school_education_id_RGMU': 'id_GRMU_school1',
                                       'school_education_statement_amount': '55566788',
                                       'school_education_link': 'http:\\my_link_1234.com',
                                       'needing_premises_id_RGMU': 'id_GRMU_residental1',
                                       'needing_premises_statement_amount': '55566788',
                                       'needing_premises_link': 'http:\\my_link_1234.com',
                                       'town_planning_id_RGMU': 'id_GRMU_town1',
                                       'town_planning_statement_amount': '55566788',
                                       'town_planning_link': 'http:\\my_link_1234.com',
                                       'archive_reference_id_RGMU': 'id_GRMU_archive1',
                                       'archive_reference_statement_amount': '55566788',
                                       'archive_reference_link': 'http:\\my_link_1234.com',
                                       'land_schemes_id_RGMU': 'id_GRMU_land1',
                                       'land_schemes_statement_amount': '55566788',
                                       'land_schemes_link': 'http:\\my_link_1234.com',
                                       'month': str(datetime.today().strftime('%m')),
                                       'year': str(datetime.today().strftime('%Y'))
                                       })

        return render(request, 'app/self_examination_form.html', {
            'region_form': region_form,
            'username': request.user.username
        })
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required(login_url='/login/',
                redirect_field_name='/result_form/residential_premises/' + datetime.today().strftime('%Y/%m/'))
def get_result_form(request, service_name, year, month):
    objects = list()

    if service_name == 'residential_premises':
        full_service_name = 'Прием заявлений и выдача документов о согласовании проведения переустройства и (или) ' \
                            'перепланировки жилого помещения '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw('''SELECT id, region_name,
                    residential_premises_id_RGMU AS id_RGMU,
                    residential_premises_statement_amount AS statement_amount,
                    residential_premises_link AS link,
                    residential_premises_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    residential_premises_has_btn_get_service_comment AS has_btn_get_service_comment,
                    residential_premises_has_reglament_comment AS has_reglament_comment,
                    residential_premises_has_estimation_quality_comment AS has_estimation_quality_comment,
                    residential_premises_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    residential_premises_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    residential_premises_has_edition_draft_comment AS has_edition_draft_comment,
                    residential_premises_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    residential_premises_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    residential_premises_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    residential_premises_has_sample_document_comment AS has_sample_document_comment,
                    residential_premises_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                    month) + '''\' AND year=\'''' + str(
                    year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)

            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'housing_transfer':
        full_service_name = 'Принятие решений о переводе жилых помещений в нежилые помещения и нежилых помещений в ' \
                            'жилые помещения '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    housing_transfer_id_RGMU AS id_RGMU,
                    housing_transfer_statement_amount AS statement_amount,
                    housing_transfer_link AS link,
                    housing_transfer_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    housing_transfer_has_btn_get_service_comment AS has_btn_get_service_comment,
                    housing_transfer_has_reglament_comment AS has_reglament_comment,
                    housing_transfer_has_estimation_quality_comment AS has_estimation_quality_comment,
                    housing_transfer_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    housing_transfer_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    housing_transfer_has_edition_draft_comment AS has_edition_draft_comment,
                    housing_transfer_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    housing_transfer_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    housing_transfer_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    housing_transfer_has_sample_document_comment AS has_sample_document_comment,
                    housing_transfer_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'advertising_structures':
        full_service_name = 'Выдача разрешения на установку и эксплуатацию рекламной конструкции'
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    advertising_structures_id_RGMU AS id_RGMU,
                    advertising_structures_statement_amount AS statement_amount,
                    advertising_structures_link AS link,
                    advertising_structures_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    advertising_structures_has_btn_get_service_comment AS has_btn_get_service_comment,
                    advertising_structures_has_reglament_comment AS has_reglament_comment,
                    advertising_structures_has_estimation_quality_comment AS has_estimation_quality_comment,
                    advertising_structures_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    advertising_structures_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    advertising_structures_has_edition_draft_comment AS has_edition_draft_comment,
                    advertising_structures_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    advertising_structures_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    advertising_structures_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    advertising_structures_has_sample_document_comment AS has_sample_document_comment,
                    advertising_structures_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'capital_construction':
        full_service_name = 'Выдача разрешения на строительство, реконструкцию объектов капитального строительства'
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    capital_construction_id_RGMU AS id_RGMU,
                    capital_construction_statement_amount AS statement_amount,
                    capital_construction_link AS link,
                    capital_construction_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    capital_construction_has_btn_get_service_comment AS has_btn_get_service_comment,
                    capital_construction_has_reglament_comment AS has_reglament_comment,
                    capital_construction_has_estimation_quality_comment AS has_estimation_quality_comment,
                    capital_construction_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    capital_construction_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    capital_construction_has_edition_draft_comment AS has_edition_draft_comment,
                    capital_construction_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    capital_construction_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    capital_construction_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    capital_construction_has_sample_document_comment AS has_sample_document_comment,
                    capital_construction_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'preschool_education':
        full_service_name = 'Прием заявлений, постановка на учет и зачисление детей в образовательные учреждения, ' \
                            'реализующие основную образовательную программу дошкольного образования (детские сады) '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    preschool_education_id_RGMU AS id_RGMU,
                    preschool_education_statement_amount AS statement_amount,
                    preschool_education_link AS link,
                    preschool_education_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    preschool_education_has_btn_get_service_comment AS has_btn_get_service_comment,
                    preschool_education_has_reglament_comment AS has_reglament_comment,
                    preschool_education_has_estimation_quality_comment AS has_estimation_quality_comment,
                    preschool_education_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    preschool_education_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    preschool_education_has_edition_draft_comment AS has_edition_draft_comment,
                    preschool_education_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    preschool_education_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    preschool_education_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    preschool_education_has_sample_document_comment AS has_sample_document_comment,
                    preschool_education_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'school_education':
        full_service_name = 'Зачисление детей в общеобразовательные учреждения субъектов Российской Федерации или ' \
                            'муниципальные общеобразовательные учреждения '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    school_education_id_RGMU AS id_RGMU,
                    school_education_statement_amount AS statement_amount,
                    school_education_link AS link,
                    school_education_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    school_education_has_btn_get_service_comment AS has_btn_get_service_comment,
                    school_education_has_reglament_comment AS has_reglament_comment,
                    school_education_has_estimation_quality_comment AS has_estimation_quality_comment,
                    school_education_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    school_education_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    school_education_has_edition_draft_comment AS has_edition_draft_comment,
                    school_education_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    school_education_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    school_education_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    school_education_has_sample_document_comment AS has_sample_document_comment,
                    school_education_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'needing_premises':
        full_service_name = 'Принятие на учет граждан в качестве нуждающихся в жилых помещениях'
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    needing_premises_id_RGMU AS id_RGMU,
                    needing_premises_statement_amount AS statement_amount,
                    needing_premises_link AS link,
                    needing_premises_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    needing_premises_has_btn_get_service_comment AS has_btn_get_service_comment,
                    needing_premises_has_reglament_comment AS has_reglament_comment,
                    needing_premises_has_estimation_quality_comment AS has_estimation_quality_comment,
                    needing_premises_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    needing_premises_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    needing_premises_has_edition_draft_comment AS has_edition_draft_comment,
                    needing_premises_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    needing_premises_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    needing_premises_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    needing_premises_has_sample_document_comment AS has_sample_document_comment,
                    needing_premises_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'town_planning':
        full_service_name = 'Выдача градостроительных планов земельных участков'
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    town_planning_id_RGMU AS id_RGMU,
                    town_planning_statement_amount AS statement_amount,
                    town_planning_link AS link,
                    town_planning_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    town_planning_has_btn_get_service_comment AS has_btn_get_service_comment,
                    town_planning_has_reglament_comment AS has_reglament_comment,
                    town_planning_has_estimation_quality_comment AS has_estimation_quality_comment,
                    town_planning_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    town_planning_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    town_planning_has_edition_draft_comment AS has_edition_draft_comment,
                    town_planning_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    town_planning_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    town_planning_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    town_planning_has_sample_document_comment AS has_sample_document_comment,
                    town_planning_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'archive_reference':
        full_service_name = 'Предоставление архивных справок, архивных копий, архивных выписок, информационных писем, ' \
                            'связанных с реализацией законных прав и свобод граждан и исполнением государственными ' \
                            'органами и органами местного самоуправления своих полномочий '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    archive_reference_id_RGMU AS id_RGMU,
                    archive_reference_statement_amount AS statement_amount,
                    archive_reference_link AS link,
                    archive_reference_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    archive_reference_has_btn_get_service_comment AS has_btn_get_service_comment,
                    archive_reference_has_reglament_comment AS has_reglament_comment,
                    archive_reference_has_estimation_quality_comment AS has_estimation_quality_comment,
                    archive_reference_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    archive_reference_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    archive_reference_has_edition_draft_comment AS has_edition_draft_comment,
                    archive_reference_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    archive_reference_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    archive_reference_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    archive_reference_has_sample_document_comment AS has_sample_document_comment,
                    archive_reference_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    elif service_name == 'land_schemes':
        full_service_name = 'Утверждение схемы расположения земельного участка или земельных участков на кадастровом ' \
                            'плане территории '
        for name in regions_names:
            try:
                obj = RegionModel.objects.raw(
                    '''SELECT id, region_name,
                    land_schemes_id_RGMU AS id_RGMU,
                    land_schemes_statement_amount AS statement_amount,
                    land_schemes_link AS link,
                    land_schemes_has_advanced_appointment_comment AS has_advanced_appointment_comment,
                    land_schemes_has_btn_get_service_comment AS has_btn_get_service_comment,
                    land_schemes_has_reglament_comment AS has_reglament_comment,
                    land_schemes_has_estimation_quality_comment AS has_estimation_quality_comment,
                    land_schemes_connected_to_FGIS_DO_comment AS connected_to_FGIS_DO_comment,
                    land_schemes_has_electronic_form_printing_comment AS has_electronic_form_printing_comment,
                    land_schemes_has_edition_draft_comment AS has_edition_draft_comment,
                    land_schemes_has_term_of_consideration_comment AS has_term_of_consideration_comment,
                    land_schemes_has_notif_consider_result_comment AS has_notif_consider_result_comment,
                    land_schemes_has_causes_of_failure_comment AS has_causes_of_failure_comment,
                    land_schemes_has_sample_document_comment AS has_sample_document_comment,
                    land_schemes_has_document_template_comment AS has_document_template_comment
                    FROM catalog_regionModel
                    WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' + str(
                        month) + '''\' AND year=\'''' + str(
                        year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]
                objects.append(obj)
            except IndexError:
                obj = {'region_name': name, 'id_RGMU': "", 'statement_amount': "", 'link': "",
                       'has_advanced_appointment_comment': "", 'has_btn_get_service_comment': "",
                       'has_reglament_comment': "", 'has_estimation_quality_comment': "",
                       'connected_to_FGIS_DO_comment': "", 'has_electronic_form_printing_comment': "",
                       'has_edition_draft_comment': "", 'has_term_of_consideration_comment': "",
                       'has_notif_consider_result_comment': "", 'has_causes_of_failure_comment': "",
                       'has_sample_document_comment': "", 'has_document_template_comment': ""}
                objects.append(dotDict(obj))

    else:
        return HttpResponseNotFound('')

    return render(request, 'app/result_form.html', {'objects': objects,
                                                        'year': str(year),
                                                        'month': str(month),
                                                        'full_service_name': full_service_name,
                                                        'service_name': service_name,
                                                        'zipped': zip(regions_names, short_regions_names),
                                                    'username': request.user.username})


@login_required(login_url='/login/',
                redirect_field_name='/result_form/residential_premises/' + datetime.today().strftime('%Y/%m/'))
def get_region_form(request, year, month, short_region_name):
    full_region_name = regions_names[short_regions_names.index(short_region_name)]
    try:
        object = RegionModel.objects.raw(
            '''SELECT id,
            residential_premises_id_RGMU,
            residential_premises_statement_amount, 
            residential_premises_link,
            residential_premises_has_advanced_appointment_comment,
            residential_premises_has_btn_get_service_comment,
            residential_premises_has_reglament_comment,
            residential_premises_has_estimation_quality_comment,
            residential_premises_connected_to_FGIS_DO_comment,
            residential_premises_has_electronic_form_printing_comment,
            residential_premises_has_edition_draft_comment,
            residential_premises_has_term_of_consideration_comment,
            residential_premises_has_notif_consider_result_comment,
            residential_premises_has_causes_of_failure_comment,
            residential_premises_has_sample_document_comment,
            residential_premises_has_document_template_comment,
            housing_transfer_id_RGMU,
            housing_transfer_statement_amount, 
            housing_transfer_link,
            housing_transfer_has_advanced_appointment_comment,
            housing_transfer_has_btn_get_service_comment,
            housing_transfer_has_reglament_comment,
            housing_transfer_has_estimation_quality_comment,
            housing_transfer_connected_to_FGIS_DO_comment,
            housing_transfer_has_electronic_form_printing_comment,
            housing_transfer_has_edition_draft_comment,
            housing_transfer_has_term_of_consideration_comment,
            housing_transfer_has_notif_consider_result_comment,
            housing_transfer_has_causes_of_failure_comment,
            housing_transfer_has_sample_document_comment,
            housing_transfer_has_document_template_comment,
            advertising_structures_id_RGMU,
            advertising_structures_statement_amount, 
            advertising_structures_link,
            advertising_structures_has_advanced_appointment_comment,
            advertising_structures_has_btn_get_service_comment,
            advertising_structures_has_reglament_comment,
            advertising_structures_has_estimation_quality_comment,
            advertising_structures_connected_to_FGIS_DO_comment,
            advertising_structures_has_electronic_form_printing_comment,
            advertising_structures_has_edition_draft_comment,
            advertising_structures_has_term_of_consideration_comment,
            advertising_structures_has_notif_consider_result_comment,
            advertising_structures_has_causes_of_failure_comment,
            advertising_structures_has_sample_document_comment,
            advertising_structures_has_document_template_comment,
            capital_construction_id_RGMU,
            capital_construction_statement_amount, 
            capital_construction_link,
            capital_construction_has_advanced_appointment_comment,
            capital_construction_has_btn_get_service_comment,
            capital_construction_has_reglament_comment,
            capital_construction_has_estimation_quality_comment,
            capital_construction_connected_to_FGIS_DO_comment,
            capital_construction_has_electronic_form_printing_comment,
            capital_construction_has_edition_draft_comment,
            capital_construction_has_term_of_consideration_comment,
            capital_construction_has_notif_consider_result_comment,
            capital_construction_has_causes_of_failure_comment,
            capital_construction_has_sample_document_comment,
            capital_construction_has_document_template_comment,
            preschool_education_id_RGMU,
            preschool_education_statement_amount, 
            preschool_education_link,
            preschool_education_has_advanced_appointment_comment,
            preschool_education_has_btn_get_service_comment,
            preschool_education_has_reglament_comment,
            preschool_education_has_estimation_quality_comment,
            preschool_education_connected_to_FGIS_DO_comment,
            preschool_education_has_electronic_form_printing_comment,
            preschool_education_has_edition_draft_comment,
            preschool_education_has_term_of_consideration_comment,
            preschool_education_has_notif_consider_result_comment,
            preschool_education_has_causes_of_failure_comment,
            preschool_education_has_sample_document_comment,
            preschool_education_has_document_template_comment,
            school_education_id_RGMU,
            school_education_statement_amount, 
            school_education_link,
            school_education_has_advanced_appointment_comment,
            school_education_has_btn_get_service_comment,
            school_education_has_reglament_comment,
            school_education_has_estimation_quality_comment,
            school_education_connected_to_FGIS_DO_comment,
            school_education_has_electronic_form_printing_comment,
            school_education_has_edition_draft_comment,
            school_education_has_term_of_consideration_comment,
            school_education_has_notif_consider_result_comment,
            school_education_has_causes_of_failure_comment,
            school_education_has_sample_document_comment,
            school_education_has_document_template_comment,
            needing_premises_id_RGMU,
            needing_premises_statement_amount, 
            needing_premises_link,
            needing_premises_has_advanced_appointment_comment,
            needing_premises_has_btn_get_service_comment,
            needing_premises_has_reglament_comment,
            needing_premises_has_estimation_quality_comment,
            needing_premises_connected_to_FGIS_DO_comment,
            needing_premises_has_electronic_form_printing_comment,
            needing_premises_has_edition_draft_comment,
            needing_premises_has_term_of_consideration_comment,
            needing_premises_has_notif_consider_result_comment,
            needing_premises_has_causes_of_failure_comment,
            needing_premises_has_sample_document_comment,
            needing_premises_has_document_template_comment,
            town_planning_id_RGMU,
            town_planning_statement_amount, 
            town_planning_link,
            town_planning_has_advanced_appointment_comment,
            town_planning_has_btn_get_service_comment,
            town_planning_has_reglament_comment,
            town_planning_has_estimation_quality_comment,
            town_planning_connected_to_FGIS_DO_comment,
            town_planning_has_electronic_form_printing_comment,
            town_planning_has_edition_draft_comment,
            town_planning_has_term_of_consideration_comment,
            town_planning_has_notif_consider_result_comment,
            town_planning_has_causes_of_failure_comment,
            town_planning_has_sample_document_comment,
            town_planning_has_document_template_comment,
            archive_reference_id_RGMU,
            archive_reference_statement_amount, 
            archive_reference_link,
            archive_reference_has_advanced_appointment_comment,
            archive_reference_has_btn_get_service_comment,
            archive_reference_has_reglament_comment,
            archive_reference_has_estimation_quality_comment,
            archive_reference_connected_to_FGIS_DO_comment,
            archive_reference_has_electronic_form_printing_comment,
            archive_reference_has_edition_draft_comment,
            archive_reference_has_term_of_consideration_comment,
            archive_reference_has_notif_consider_result_comment,
            archive_reference_has_causes_of_failure_comment,
            archive_reference_has_sample_document_comment,
            archive_reference_has_document_template_comment,
            land_schemes_id_RGMU,
            land_schemes_statement_amount, 
            land_schemes_link,
            land_schemes_has_advanced_appointment_comment,
            land_schemes_has_btn_get_service_comment,
            land_schemes_has_reglament_comment,
            land_schemes_has_estimation_quality_comment,
            land_schemes_connected_to_FGIS_DO_comment,
            land_schemes_has_electronic_form_printing_comment,
            land_schemes_has_edition_draft_comment,
            land_schemes_has_term_of_consideration_comment,
            land_schemes_has_notif_consider_result_comment,
            land_schemes_has_causes_of_failure_comment,
            land_schemes_has_sample_document_comment,
            land_schemes_has_document_template_comment
            FROM catalog_regionModel
            WHERE region_name =\'''' + str(full_region_name) + '''\' AND month=\'''' + str(
                month) + '''\' AND year=\'''' + str(
                year) + '''\' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;''')[0]

    except IndexError:
        object = {'short_region_name': short_region_name,
                  'residential_premises_id_RGMU': "",
                  'residential_premises_statement_amount': "",
                  'residential_premises_link': "",
                  'residential_premises_has_advanced_appointment_comment': "",
                  'residential_premises_has_btn_get_service_comment': "",
                  'residential_premises_has_reglament_comment': "",
                  'residential_premises_has_estimation_quality_comment': "",
                  'residential_premises_connected_to_FGIS_DO_comment': "",
                  'residential_premises_has_electronic_form_printing_comment': "",
                  'residential_premises_has_edition_draft_comment': "",
                  'residential_premises_has_term_of_consideration_comment': "",
                  'residential_premises_has_notif_consider_result_comment': "",
                  'residential_premises_has_causes_of_failure_comment': "",
                  'residential_premises_has_sample_document_comment': "",
                  'esidential_premises_has_document_template_comment': "",
                  'rousing_transfer_id_RGMU': "",
                  'housing_transfer_statement_amount': "",
                  'housing_transfer_link': "",
                  'housing_transfer_has_advanced_appointment_comment': "",
                  'housing_transfer_has_btn_get_service_comment': "",
                  'housing_transfer_has_reglament_comment': "",
                  'housing_transfer_has_estimation_quality_comment': "",
                  'housing_transfer_connected_to_FGIS_DO_comment': "",
                  'housing_transfer_has_electronic_form_printing_comment': "",
                  'housing_transfer_has_edition_draft_comment': "",
                  'housing_transfer_has_term_of_consideration_comment': "",
                  'housing_transfer_has_notif_consider_result_comment': "",
                  'housing_transfer_has_causes_of_failure_comment': "",
                  'housing_transfer_has_sample_document_comment': "",
                  'housing_transfer_has_document_template_comment': "",
                  'advertising_structures_id_RGMU': "",
                  'advertising_structures_statement_amount': "",
                  'advertising_structures_link': "",
                  'advertising_structures_has_advanced_appointment_comment': "",
                  'advertising_structures_has_btn_get_service_comment': "",
                  'advertising_structures_has_reglament_comment': "",
                  'advertising_structures_has_estimation_quality_comment': "",
                  'advertising_structures_connected_to_FGIS_DO_comment': "",
                  'advertising_structures_has_electronic_form_printing_comment': "",
                  'advertising_structures_has_edition_draft_comment': "",
                  'advertising_structures_has_term_of_consideration_comment': "",
                  'advertising_structures_has_notif_consider_result_comment': "",
                  'advertising_structures_has_causes_of_failure_comment': "",
                  'advertising_structures_has_sample_document_comment': "",
                  'advertising_structures_has_document_template_comment': "",
                  'capital_construction_id_RGMU': "",
                  'capital_construction_statement_amount': "",
                  'capital_construction_link': "",
                  'capital_construction_has_advanced_appointment_comment': "",
                  'capital_construction_has_btn_get_service_comment': "",
                  'capital_construction_has_reglament_comment': "",
                  'capital_construction_has_estimation_quality_comment': "",
                  'capital_construction_connected_to_FGIS_DO_comment': "",
                  'capital_construction_has_electronic_form_printing_comment': "",
                  'capital_construction_has_edition_draft_comment': "",
                  'capital_construction_has_term_of_consideration_comment': "",
                  'capital_construction_has_notif_consider_result_comment': "",
                  'capital_construction_has_causes_of_failure_comment': "",
                  'capital_construction_has_sample_document_comment': "",
                  'capital_construction_has_document_template_comment': "",
                  'preschool_education_id_RGMU': "",
                  'preschool_education_statement_amount': "",
                  'preschool_education_link': "",
                  'preschool_education_has_advanced_appointment_comment': "",
                  'preschool_education_has_btn_get_service_comment': "",
                  'preschool_education_has_reglament_comment': "",
                  'preschool_education_has_estimation_quality_comment': "",
                  'preschool_education_connected_to_FGIS_DO_comment': "",
                  'preschool_education_has_electronic_form_printing_comment': "",
                  'preschool_education_has_edition_draft_comment': "",
                  'preschool_education_has_term_of_consideration_comment': "",
                  'preschool_education_has_notif_consider_result_comment': "",
                  'preschool_education_has_causes_of_failure_comment': "",
                  'preschool_education_has_sample_document_comment': "",
                  'preschool_education_has_document_template_comment': "",
                  'school_education_id_RGMU': "",
                  'school_education_statement_amount': "",
                  'school_education_link': "",
                  'school_education_has_advanced_appointment_comment': "",
                  'school_education_has_btn_get_service_comment': "",
                  'school_education_has_reglament_comment': "",
                  'school_education_has_estimation_quality_comment': "",
                  'school_education_connected_to_FGIS_DO_comment': "",
                  'school_education_has_electronic_form_printing_comment': "",
                  'school_education_has_edition_draft_comment': "",
                  'school_education_has_term_of_consideration_comment': "",
                  'school_education_has_notif_consider_result_comment': "",
                  'school_education_has_causes_of_failure_comment': "",
                  'school_education_has_sample_document_comment': "",
                  'school_education_has_document_template_comment': "",
                  'needing_premises_id_RGMU': "",
                  'needing_premises_statement_amount': "",
                  'needing_premises_link': "",
                  'needing_premises_has_advanced_appointment_comment': "",
                  'needing_premises_has_btn_get_service_comment': "",
                  'needing_premises_has_reglament_comment': "",
                  'needing_premises_has_estimation_quality_comment': "",
                  'needing_premises_connected_to_FGIS_DO_comment': "",
                  'needing_premises_has_electronic_form_printing_comment': "",
                  'needing_premises_has_edition_draft_comment': "",
                  'needing_premises_has_term_of_consideration_comment': "",
                  'needing_premises_has_notif_consider_result_comment': "",
                  'needing_premises_has_causes_of_failure_comment': "",
                  'needing_premises_has_sample_document_comment': "",
                  'needing_premises_has_document_template_comment': "",
                  'town_planning_id_RGMU': "",
                  'town_planning_statement_amount': "",
                  'town_planning_link': "",
                  'town_planning_has_advanced_appointment_comment': "",
                  'town_planning_has_btn_get_service_comment': "",
                  'town_planning_has_reglament_comment': "",
                  'town_planning_has_estimation_quality_comment': "",
                  'town_planning_connected_to_FGIS_DO_comment': "",
                  'town_planning_has_electronic_form_printing_comment': "",
                  'town_planning_has_edition_draft_comment': "",
                  'town_planning_has_term_of_consideration_comment': "",
                  'town_planning_has_notif_consider_result_comment': "",
                  'town_planning_has_causes_of_failure_comment': "",
                  'town_planning_has_sample_document_comment': "",
                  'town_planning_has_document_template_comment': "",
                  'archive_reference_id_RGMU': "",
                  'archive_reference_statement_amount': "",
                  'archive_reference_link': "",
                  'archive_reference_has_advanced_appointment_comment': "",
                  'archive_reference_has_btn_get_service_comment': "",
                  'archive_reference_has_reglament_comment': "",
                  'archive_reference_has_estimation_quality_comment': "",
                  'archive_reference_connected_to_FGIS_DO_comment': "",
                  'archive_reference_has_electronic_form_printing_comment': "",
                  'archive_reference_has_edition_draft_comment': "",
                  'archive_reference_has_term_of_consideration_comment': "",
                  'archive_reference_has_notif_consider_result_comment': "",
                  'archive_reference_has_causes_of_failure_comment': "",
                  'archive_reference_has_sample_document_comment': "",
                  'archive_reference_has_document_template_comment': "",
                  'land_schemes_id_RGMU': "",
                  'land_schemes_statement_amount': "",
                  'land_schemes_link': "",
                  'land_schemes_has_advanced_appointment_comment': "",
                  'land_schemes_has_btn_get_service_comment': "",
                  'land_schemes_has_reglament_comment': "",
                  'land_schemes_has_estimation_quality_comment': "",
                  'land_schemes_connected_to_FGIS_DO_comment': "",
                  'land_schemes_has_electronic_form_printing_comment': "",
                  'land_schemes_has_edition_draft_comment': "",
                  'land_schemes_has_term_of_consideration_comment': "",
                  'land_schemes_has_notif_consider_result_comment': "",
                  'land_schemes_has_causes_of_failure_comment': "",
                  'land_schemes_has_sample_document_comment': "",
                  'land_schemes_has_document_template_comment': ""
                  }
    return render(request, 'app/region_form.html', {'object': object,
                                                        'year': str(year),
                                                        'month': str(month),
                                                        'zipped': zip(regions_names, short_regions_names),
                                                        'full_region_name': full_region_name,
                                                        'short_region_name': short_region_name,
                                                    'username': request.user.username
                                                    })


@login_required(login_url='/login/',
                redirect_field_name='/result_form/residential_premises/' + datetime.today().strftime('%Y/%m/'))
def get_result_form_with_troubles(request, year, month):
    objects = dict()
    objects.update({'residential_premises': []})
    objects.update({'housing_transfer': []})
    objects.update({'advertising_structures': []})
    objects.update({'capital_construction': []})
    objects.update({'preschool_education': []})
    objects.update({'school_education': []})
    objects.update({'needing_premises': []})
    objects.update({'town_planning': []})
    objects.update({'archive_reference': []})
    objects.update({'land_schemes': []})
    for name in regions_names:
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    residential_premises_id_RGMU,
                    residential_premises_statement_amount,
                    residential_premises_link,
                    residential_premises_has_advanced_appointment_comment,
                    residential_premises_has_btn_get_service_comment,
                    residential_premises_has_reglament_comment,
                    residential_premises_has_estimation_quality_comment,
                    residential_premises_connected_to_FGIS_DO_comment,
                    residential_premises_has_electronic_form_printing_comment,
                    residential_premises_has_edition_draft_comment,
                    residential_premises_has_term_of_consideration_comment,
                    residential_premises_has_notif_consider_result_comment,
                    residential_premises_has_causes_of_failure_comment,
                    residential_premises_has_sample_document_comment,
                    residential_premises_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((residential_premises_has_advanced_appointment_comment != \'Да\' AND\
                    residential_premises_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_btn_get_service_comment != \'Да\' AND\
                    residential_premises_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_reglament_comment != \'Да\' AND\
                    residential_premises_has_reglament_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_estimation_quality_comment != \'Да\' AND\
                    residential_premises_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (residential_premises_connected_to_FGIS_DO_comment != \'Да\' AND\
                    residential_premises_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_electronic_form_printing_comment != \'Да\' AND\
                    residential_premises_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_edition_draft_comment != \'Да\' AND\
                    residential_premises_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_term_of_consideration_comment != \'Да\' AND\
                    residential_premises_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_notif_consider_result_comment != \'Да\' AND\
                    residential_premises_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_causes_of_failure_comment != \'Да\' AND\
                    residential_premises_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_sample_document_comment != \'Да\' AND\
                    residential_premises_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (residential_premises_has_document_template_comment != \'Да\' AND\
                    residential_premises_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['residential_premises'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    housing_transfer_id_RGMU,
                    housing_transfer_statement_amount,
                    housing_transfer_link,
                    housing_transfer_has_advanced_appointment_comment,
                    housing_transfer_has_btn_get_service_comment,
                    housing_transfer_has_reglament_comment,
                    housing_transfer_has_estimation_quality_comment,
                    housing_transfer_connected_to_FGIS_DO_comment,
                    housing_transfer_has_electronic_form_printing_comment,
                    housing_transfer_has_edition_draft_comment,
                    housing_transfer_has_term_of_consideration_comment,
                    housing_transfer_has_notif_consider_result_comment,
                    housing_transfer_has_causes_of_failure_comment,
                    housing_transfer_has_sample_document_comment,
                    housing_transfer_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((housing_transfer_has_advanced_appointment_comment != \'Да\' AND\
                    housing_transfer_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_btn_get_service_comment != \'Да\' AND\
                    housing_transfer_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_reglament_comment != \'Да\' AND\
                    housing_transfer_has_reglament_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_estimation_quality_comment != \'Да\' AND\
                    housing_transfer_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_connected_to_FGIS_DO_comment != \'Да\' AND\
                    housing_transfer_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_electronic_form_printing_comment != \'Да\' AND\
                    housing_transfer_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_edition_draft_comment != \'Да\' AND\
                    housing_transfer_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_term_of_consideration_comment != \'Да\' AND\
                    housing_transfer_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_notif_consider_result_comment != \'Да\' AND\
                    housing_transfer_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_causes_of_failure_comment != \'Да\' AND\
                    housing_transfer_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_sample_document_comment != \'Да\' AND\
                    housing_transfer_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (housing_transfer_has_document_template_comment != \'Да\' AND\
                    housing_transfer_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['housing_transfer'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    advertising_structures_id_RGMU,
                    advertising_structures_statement_amount,
                    advertising_structures_link,
                    advertising_structures_has_advanced_appointment_comment,
                    advertising_structures_has_btn_get_service_comment,
                    advertising_structures_has_reglament_comment,
                    advertising_structures_has_estimation_quality_comment,
                    advertising_structures_connected_to_FGIS_DO_comment,
                    advertising_structures_has_electronic_form_printing_comment,
                    advertising_structures_has_edition_draft_comment,
                    advertising_structures_has_term_of_consideration_comment,
                    advertising_structures_has_notif_consider_result_comment,
                    advertising_structures_has_causes_of_failure_comment,
                    advertising_structures_has_sample_document_comment,
                    advertising_structures_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((advertising_structures_has_advanced_appointment_comment != \'Да\' AND\
                    advertising_structures_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_btn_get_service_comment != \'Да\' AND\
                    advertising_structures_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_reglament_comment != \'Да\' AND\
                    advertising_structures_has_reglament_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_estimation_quality_comment != \'Да\' AND\
                    advertising_structures_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_connected_to_FGIS_DO_comment != \'Да\' AND\
                    advertising_structures_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_electronic_form_printing_comment != \'Да\' AND\
                    advertising_structures_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_edition_draft_comment != \'Да\' AND\
                    advertising_structures_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_term_of_consideration_comment != \'Да\' AND\
                    advertising_structures_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_notif_consider_result_comment != \'Да\' AND\
                    advertising_structures_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_causes_of_failure_comment != \'Да\' AND\
                    advertising_structures_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_sample_document_comment != \'Да\' AND\
                    advertising_structures_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (advertising_structures_has_document_template_comment != \'Да\' AND\
                    advertising_structures_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['advertising_structures'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    capital_construction_id_RGMU,
                    capital_construction_statement_amount,
                    capital_construction_link,
                    capital_construction_has_advanced_appointment_comment,
                    capital_construction_has_btn_get_service_comment,
                    capital_construction_has_reglament_comment,
                    capital_construction_has_estimation_quality_comment,
                    capital_construction_connected_to_FGIS_DO_comment,
                    capital_construction_has_electronic_form_printing_comment,
                    capital_construction_has_edition_draft_comment,
                    capital_construction_has_term_of_consideration_comment,
                    capital_construction_has_notif_consider_result_comment,
                    capital_construction_has_causes_of_failure_comment,
                    capital_construction_has_sample_document_comment,
                    capital_construction_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((capital_construction_has_advanced_appointment_comment != \'Да\' AND\
                    capital_construction_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_btn_get_service_comment != \'Да\' AND\
                    capital_construction_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_reglament_comment != \'Да\' AND\
                    capital_construction_has_reglament_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_estimation_quality_comment != \'Да\' AND\
                    capital_construction_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (capital_construction_connected_to_FGIS_DO_comment != \'Да\' AND\
                    capital_construction_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_electronic_form_printing_comment != \'Да\' AND\
                    capital_construction_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_edition_draft_comment != \'Да\' AND\
                    capital_construction_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_term_of_consideration_comment != \'Да\' AND\
                    capital_construction_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_notif_consider_result_comment != \'Да\' AND\
                    capital_construction_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_causes_of_failure_comment != \'Да\' AND\
                    capital_construction_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_sample_document_comment != \'Да\' AND\
                    capital_construction_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (capital_construction_has_document_template_comment != \'Да\' AND\
                    capital_construction_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['capital_construction'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    preschool_education_id_RGMU,
                    preschool_education_statement_amount,
                    preschool_education_link,
                    preschool_education_has_advanced_appointment_comment,
                    preschool_education_has_btn_get_service_comment,
                    preschool_education_has_reglament_comment,
                    preschool_education_has_estimation_quality_comment,
                    preschool_education_connected_to_FGIS_DO_comment,
                    preschool_education_has_electronic_form_printing_comment,
                    preschool_education_has_edition_draft_comment,
                    preschool_education_has_term_of_consideration_comment,
                    preschool_education_has_notif_consider_result_comment,
                    preschool_education_has_causes_of_failure_comment,
                    preschool_education_has_sample_document_comment,
                    preschool_education_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((preschool_education_has_advanced_appointment_comment != \'Да\' AND\
                    preschool_education_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_btn_get_service_comment != \'Да\' AND\
                    preschool_education_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_reglament_comment != \'Да\' AND\
                    preschool_education_has_reglament_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_estimation_quality_comment != \'Да\' AND\
                    preschool_education_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (preschool_education_connected_to_FGIS_DO_comment != \'Да\' AND\
                    preschool_education_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_electronic_form_printing_comment != \'Да\' AND\
                    preschool_education_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_edition_draft_comment != \'Да\' AND\
                    preschool_education_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_term_of_consideration_comment != \'Да\' AND\
                    preschool_education_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_notif_consider_result_comment != \'Да\' AND\
                    preschool_education_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_causes_of_failure_comment != \'Да\' AND\
                    preschool_education_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_sample_document_comment != \'Да\' AND\
                    preschool_education_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (preschool_education_has_document_template_comment != \'Да\' AND\
                    preschool_education_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['preschool_education'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    school_education_id_RGMU,
                    school_education_statement_amount,
                    school_education_link,
                    school_education_has_advanced_appointment_comment,
                    school_education_has_btn_get_service_comment,
                    school_education_has_reglament_comment,
                    school_education_has_estimation_quality_comment,
                    school_education_connected_to_FGIS_DO_comment,
                    school_education_has_electronic_form_printing_comment,
                    school_education_has_edition_draft_comment,
                    school_education_has_term_of_consideration_comment,
                    school_education_has_notif_consider_result_comment,
                    school_education_has_causes_of_failure_comment,
                    school_education_has_sample_document_comment,
                    school_education_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((school_education_has_advanced_appointment_comment != \'Да\' AND\
                    school_education_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (school_education_has_btn_get_service_comment != \'Да\' AND\
                    school_education_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (school_education_has_reglament_comment != \'Да\' AND\
                    school_education_has_reglament_comment != \'Не предусмотрено\') OR\
                    (school_education_has_estimation_quality_comment != \'Да\' AND\
                    school_education_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (school_education_connected_to_FGIS_DO_comment != \'Да\' AND\
                    school_education_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (school_education_has_electronic_form_printing_comment != \'Да\' AND\
                    school_education_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (school_education_has_edition_draft_comment != \'Да\' AND\
                    school_education_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (school_education_has_term_of_consideration_comment != \'Да\' AND\
                    school_education_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (school_education_has_notif_consider_result_comment != \'Да\' AND\
                    school_education_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (school_education_has_causes_of_failure_comment != \'Да\' AND\
                    school_education_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (school_education_has_sample_document_comment != \'Да\' AND\
                    school_education_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (school_education_has_document_template_comment != \'Да\' AND\
                    school_education_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['school_education'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    needing_premises_id_RGMU,
                    needing_premises_statement_amount,
                    needing_premises_link,
                    needing_premises_has_advanced_appointment_comment,
                    needing_premises_has_btn_get_service_comment,
                    needing_premises_has_reglament_comment,
                    needing_premises_has_estimation_quality_comment,
                    needing_premises_connected_to_FGIS_DO_comment,
                    needing_premises_has_electronic_form_printing_comment,
                    needing_premises_has_edition_draft_comment,
                    needing_premises_has_term_of_consideration_comment,
                    needing_premises_has_notif_consider_result_comment,
                    needing_premises_has_causes_of_failure_comment,
                    needing_premises_has_sample_document_comment,
                    needing_premises_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((needing_premises_has_advanced_appointment_comment != \'Да\' AND\
                    needing_premises_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_btn_get_service_comment != \'Да\' AND\
                    needing_premises_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_reglament_comment != \'Да\' AND\
                    needing_premises_has_reglament_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_estimation_quality_comment != \'Да\' AND\
                    needing_premises_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (needing_premises_connected_to_FGIS_DO_comment != \'Да\' AND\
                    needing_premises_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_electronic_form_printing_comment != \'Да\' AND\
                    needing_premises_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_edition_draft_comment != \'Да\' AND\
                    needing_premises_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_term_of_consideration_comment != \'Да\' AND\
                    needing_premises_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_notif_consider_result_comment != \'Да\' AND\
                    needing_premises_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_causes_of_failure_comment != \'Да\' AND\
                    needing_premises_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_sample_document_comment != \'Да\' AND\
                    needing_premises_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (needing_premises_has_document_template_comment != \'Да\' AND\
                    needing_premises_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['needing_premises'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    town_planning_id_RGMU,
                    town_planning_statement_amount,
                    town_planning_link,
                    town_planning_has_advanced_appointment_comment,
                    town_planning_has_btn_get_service_comment,
                    town_planning_has_reglament_comment,
                    town_planning_has_estimation_quality_comment,
                    town_planning_connected_to_FGIS_DO_comment,
                    town_planning_has_electronic_form_printing_comment,
                    town_planning_has_edition_draft_comment,
                    town_planning_has_term_of_consideration_comment,
                    town_planning_has_notif_consider_result_comment,
                    town_planning_has_causes_of_failure_comment,
                    town_planning_has_sample_document_comment,
                    town_planning_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((town_planning_has_advanced_appointment_comment != \'Да\' AND\
                    town_planning_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_btn_get_service_comment != \'Да\' AND\
                    town_planning_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_reglament_comment != \'Да\' AND\
                    town_planning_has_reglament_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_estimation_quality_comment != \'Да\' AND\
                    town_planning_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (town_planning_connected_to_FGIS_DO_comment != \'Да\' AND\
                    town_planning_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_electronic_form_printing_comment != \'Да\' AND\
                    town_planning_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_edition_draft_comment != \'Да\' AND\
                    town_planning_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_term_of_consideration_comment != \'Да\' AND\
                    town_planning_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_notif_consider_result_comment != \'Да\' AND\
                    town_planning_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_causes_of_failure_comment != \'Да\' AND\
                    town_planning_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_sample_document_comment != \'Да\' AND\
                    town_planning_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (town_planning_has_document_template_comment != \'Да\' AND\
                    town_planning_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['town_planning'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    archive_reference_id_RGMU,
                    archive_reference_statement_amount,
                    archive_reference_link,
                    archive_reference_has_advanced_appointment_comment,
                    archive_reference_has_btn_get_service_comment,
                    archive_reference_has_reglament_comment,
                    archive_reference_has_estimation_quality_comment,
                    archive_reference_connected_to_FGIS_DO_comment,
                    archive_reference_has_electronic_form_printing_comment,
                    archive_reference_has_edition_draft_comment,
                    archive_reference_has_term_of_consideration_comment,
                    archive_reference_has_notif_consider_result_comment,
                    archive_reference_has_causes_of_failure_comment,
                    archive_reference_has_sample_document_comment,
                    archive_reference_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((archive_reference_has_advanced_appointment_comment != \'Да\' AND\
                    archive_reference_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_btn_get_service_comment != \'Да\' AND\
                    archive_reference_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_reglament_comment != \'Да\' AND\
                    archive_reference_has_reglament_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_estimation_quality_comment != \'Да\' AND\
                    archive_reference_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (archive_reference_connected_to_FGIS_DO_comment != \'Да\' AND\
                    archive_reference_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_electronic_form_printing_comment != \'Да\' AND\
                    archive_reference_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_edition_draft_comment != \'Да\' AND\
                    archive_reference_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_term_of_consideration_comment != \'Да\' AND\
                    archive_reference_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_notif_consider_result_comment != \'Да\' AND\
                    archive_reference_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_causes_of_failure_comment != \'Да\' AND\
                    archive_reference_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_sample_document_comment != \'Да\' AND\
                    archive_reference_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (archive_reference_has_document_template_comment != \'Да\' AND\
                    archive_reference_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['archive_reference'].append(obj)
        for obj in RegionModel.objects.raw(
                '''SELECT id, region_name,
                    land_schemes_id_RGMU,
                    land_schemes_statement_amount,
                    land_schemes_link,
                    land_schemes_has_advanced_appointment_comment,
                    land_schemes_has_btn_get_service_comment,
                    land_schemes_has_reglament_comment,
                    land_schemes_has_estimation_quality_comment,
                    land_schemes_connected_to_FGIS_DO_comment,
                    land_schemes_has_electronic_form_printing_comment,
                    land_schemes_has_edition_draft_comment,
                    land_schemes_has_term_of_consideration_comment,
                    land_schemes_has_notif_consider_result_comment,
                    land_schemes_has_causes_of_failure_comment,
                    land_schemes_has_sample_document_comment,
                    land_schemes_has_document_template_comment\
                    FROM catalog_regionModel WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                str(month) + '''\' AND year=\'''' + str(year) +
                '''\' AND ((land_schemes_has_advanced_appointment_comment != \'Да\' AND\
                    land_schemes_has_advanced_appointment_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_btn_get_service_comment != \'Да\' AND\
                    land_schemes_has_btn_get_service_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_reglament_comment != \'Да\' AND\
                    land_schemes_has_reglament_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_estimation_quality_comment != \'Да\' AND\
                    land_schemes_has_estimation_quality_comment != \'Не предусмотрено\') OR\
                    (land_schemes_connected_to_FGIS_DO_comment != \'Да\' AND\
                    land_schemes_connected_to_FGIS_DO_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_electronic_form_printing_comment != \'Да\' AND\
                    land_schemes_has_electronic_form_printing_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_edition_draft_comment != \'Да\' AND\
                    land_schemes_has_edition_draft_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_term_of_consideration_comment != \'Да\' AND\
                    land_schemes_has_term_of_consideration_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_notif_consider_result_comment != \'Да\' AND\
                    land_schemes_has_notif_consider_result_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_causes_of_failure_comment != \'Да\' AND\
                    land_schemes_has_causes_of_failure_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_sample_document_comment != \'Да\' AND\
                    land_schemes_has_sample_document_comment != \'Не предусмотрено\') OR\
                    (land_schemes_has_document_template_comment != \'Да\' AND\
                    land_schemes_has_document_template_comment != \'Не предусмотрено\'))'''
                + ''' ORDER BY year DESC, month DESC, day DESC, time DESC LIMIT 1;'''):
            objects['land_schemes'].append(obj)
    return render(request, 'app/filter_form.html', {'objects': dotDict(objects),
                                                        'year': str(year),
                                                        'month': str(month),
                                                        'zipped': zip(regions_names, short_regions_names),
                                                        'username': request.user.username})


@login_required(login_url='/login/',
                redirect_field_name='/result_form/residential_premises/' + datetime.today().strftime('%Y/%m/'))
def get_result_form_not_sent(request, year, month):
    objects = []
    for name in regions_names:
        try:
            obj = RegionModel.objects.raw('''
                SELECT id
                FROM catalog_regionModel 
                WHERE region_name =\'''' + str(name) + '''\' AND month=\'''' +
                                          str(month) + '''\' AND year=\'''' + str(year) + '''\'''')[0]
        except IndexError:
            objects.append(name)

    return render(request, 'app/not_sent.html', {'objects': objects,
                                                     'year': str(year),
                                                     'month': str(month),
                                                     'zipped': zip(regions_names, short_regions_names),
                                                     'username': request.user.username
                                                 })


def login_view(request):
    form = LoginForm(request.POST or None)
    print("form created",request.POST,form.is_valid())
    if request.POST and form.is_valid():
        print("request is POST")
        user = form.login(request)
        if user:
            print("user exists")
            login(request, user)
            print("hello")
            return HttpResponseRedirect(reverse('result_form', kwargs={
                'service_name': 'residential_premises',
                'year': datetime.today().strftime('%Y'),
                'month': datetime.today().strftime('%m')
            }))
    return render(request, 'app/registration/login.html', {'form': form})


def logout_view(request):
   logout(request)
   return HttpResponseRedirect('/login/')