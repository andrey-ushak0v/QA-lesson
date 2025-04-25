import requests


base_url = "http://5.101.50.27:8000"

class CompanyApi:

    def __init__(self, url):
        self.url = url

    def get_token(self):
        creds = {"username": "harrypotter", "password": "expelliarmus"}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, 'неожиданный статус ответа'
        return resp.json()['user_token']

    def create_company(self, name, description=""):
        company = {'name': name, 'description': description}
        resp = requests.post(self.url + '/company/create', json=company)
        assert resp.status_code == 201, 'неожиданный статус ответа'
        return resp.json()

    def get_company(self, company_id):
        resp = requests.get(f'{self.url}/company/{company_id}')
        assert resp.status_code == 200 or resp.status_code == 404
        return resp.json()

    def edit_company(self, company_id, new_name, new_desc):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{company_id}?client_token={client_token}"
        company = {'name': new_name, 'description': new_desc}
        resp = requests.patch(url_with_token, json=company)
        assert resp.status_code == 200, 'неожиданный статус ответа'

    def delete_company(self, company_id):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/{company_id}?client_token={client_token}"
        resp = requests.delete(url_with_token)
        assert resp.status_code == 200
        return

    def get_company_list(self):
        resp = requests.get(self.url + '/company/list')
        assert resp.status_code == 200
        return resp.json()














