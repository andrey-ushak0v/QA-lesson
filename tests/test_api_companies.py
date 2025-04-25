from base_requests import CompanyApi


base_url = "http://5.101.50.27:8000"

def test_create_company():
    api = CompanyApi(base_url)

    companies_before = api.get_company_list()
    initial_count = len(companies_before)
    api.create_company('имя', 'описание')
    companies_after = api.get_company_list()
    final_count = len(companies_after)
    assert initial_count + 1 == final_count


def test_get_one_company():
    api = CompanyApi(base_url)
    result = api.create_company('имя111', 'описани111111е')
    comp_id = result['id']
    company_by_id = api.get_company(comp_id)

    assert company_by_id['name'] == 'имя111'
    assert company_by_id['description'] == 'описани111111е'
    assert company_by_id['is_active'] is True


def test_delete_company():
    api = CompanyApi(base_url)
    name = "Company to be deleted"
    descr = "Delete me"
    result = api.create_company(name, descr)
    comp_id = result['id']

    api.delete_company(comp_id)
    deleted = api.get_company(comp_id)
    assert deleted['detail'] == "Компания не найдена", 'неожиданный ответ сервера'


