import requests
from dotenv import load_dotenv
import os

load_dotenv()

JSESSIONID = os.getenv('JSESSIONID')

headers = {
    "Accept": "application/vnd.linkedin.normalized+json+2.1",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    # "Cookie": "[long string of cookies, omitted for brevity]",
    "Csrf-Token": JSESSIONID.strip('"'),
    "Priority": "u=1, i",
    "Referer": "https://www.linkedin.com/my-items/saved-jobs/?cardType=IN_PROGRESS",
    "Sec-Ch-Ua": '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '\"macOS\"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-Li-Lang": "en_US",
    "X-Li-Page-Instance": "urn:li:page:d_flagship3_myitems_savedjobs;/A9ecWBqR7mrXD4k93VT5g==",
    "X-Li-Pem-Metadata": "Voyager - My Items=myitems-saved-jobs",
    "X-Li-Track": '{\"clientVersion\":\"1.13.20142\",\"mpVersion\":\"1.13.20142\",\"osName\":\"web\",\"timezoneOffset\":-7,\"timezone\":\"America/Los_Angeles\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":1.600000023841858,\"displayWidth\":2304.0000343322754,\"displayHeight\":1440.0000214576721}',
    "X-Restli-Protocol-Version": "2.0.0"
}

cookies = {
    "li_rm": 'AQGnT_vOShf6mQAAAZDEmU1hvMVd-yXN9erF72SOexAa0PlQWYvf-DoFWeMLwUHsupas56wKJZ9_TDExC6MPzD5bezqggRAIxgP15YsdddnD8Juk0fEyK0gG',
    'bcookie': "v=2&d4e6377b-5e2c-435c-8139-bfbc35d5e003",
    'bscookie': "v=1&20240718064819ab5eb69f-d3f0-405c-8e7e-44b05875965fAQGZ4qc3m5ueiYkGLKBBpLLFSj8CHmT7",
    '_gcl_au':'1.1.2023255331.1721285309',
    'aam_uuid':'52479637811493782440203935766855706017',
    'timezone': 'America/Los_Angeles',
    'li_theme': 'light',
    'li_theme_set': 'app',
    '_guid': '5fe5b491-c7a3-41f9-88bd-78e47c02ef3f',
    'li_sugr': 'a8977d7f-1ca8-4841-bb42-2444977ec364', 
    'AnalyticsSyncHistory': 'AQJTLih9IuKazwAAAZDEmeaMI3aLlDJKVkwXAmLzM3xAVBggRV497gXuFl3v3jXkA6sdGHtkf1oDK4adIncndw',
    'lms_ads': 'AQGMZiGkLbilGwAAAZDEmebTRxYkiq8CCllRLuNCXARrWNRnDbabHUE3X3rceL_xypHxJm9U966QZlcBJrKsdf7P22MIkVpY',
    'lms_analytics': 'AQGMZiGkLbilGwAAAZDEmebTRxYkiq8CCllRLuNCXARrWNRnDbabHUE3X3rceL_xypHxJm9U966QZlcBJrKsdf7P22MIkVpY',
    'dfpfpt': 'ba4e89be8a044015af4d54f796800e27', 
    'at_check': 'true', 
    's_fid': '0D12675185D8A2E6-04A39519A2BAFBAC',
    's_cc': 'true',
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVuNNpuPAG73YpdQnHAjkKbs3ERY%252bG3rQRxhKRbE6NbkkdSU2%252f8XHuf1SUmiJY4ai%252bySMyOT6fILonpyazELaQM8fG33K%252bZQgL6VGY0XqKXrHYElC7PejGv%252f1B0vJAF%252fZVjq32y5NpIAxA%252fUdenft55PtVrFbcI3ZwG3nDP9MTtD6f17PzoLuCY%252b5XolxW%252bS4Bxf%252fQr8d%252bxDm4IVz1I9XsOwJabVaTN7qbvea6dEOGlZx%252f5YXR%252bfm9vTNraGuxlVmQFwQpZ2fN7gedtuJqmGP6eexZ3MtadAhq156it8k%252fCfChZPsNo0p1w39%252bS%252b06AATb8%253d',
    'visit': 'v=1&M', 
    'lang': 'v=2&lang=en-us',
    # 'JSESSIONID': '\"ajax:5403365271819302899\"',
    'JSESSIONID': JSESSIONID,
    'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg':'1',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg':'-637568504%7CMCIDTS%7C19923%7CMCMID%7C51959362510172131990151901119295821418%7CMCAAMLH-1722036126%7C9%7CMCAAMB-1722036126%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721438526s%7CNONE%7CvVersion%7C5.1.1',
    'g_state': '{\"i_l\":0}',
    'liap': 'true',  
    'li_at': 'AQEDAVDhIHEB_tMeAAABkM1OVuIAAAGQ8Vra4lYAD7HVxq0Iidd51ASa9Y-IR1VFq7cBU5b-icRVX5ZTWzdx0mpji0awymydubBu5lxBOgHbn9Ux_wvJy0NzFwFRJRsUk_fDfpbxqAdnInQRg1EEACd9',
    'gpv_pn': 'developer.linkedin.com%2F',
    's_plt': '1.24', 
    's_pltp': 'developer.linkedin.com%2F', 
    's_tslv': '1721458194766',
    'mbox': 'PC#8a45615ac753415296ef9be8db9783d9.35_0#1737010196|session#179076dfe8b647c7a7dc2126f5d18031#1721460056', 
    's_ips': '814',
    's_tp': '3026',
    's_ppv': 'developer.linkedin.com%2F%2C43%2C27%2C1292%2C1%2C3',
    'sdsc': '1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D',
    'UserMatchHistory': 'AQKiCw3K0DDzjQAAAZDPAHluvCpE1UP7vBXpGj5rg9S2ugM9dHygG9XjkoI-yZBHZc_l1y_iFEUf-_FFxOCvTxf2n11QQfHWC5T7lTcLK43FwOV6Lo_PuKZGaJ-HcV_nkYhJtMiSP2w9cAzY9nqTGnPx3PAUPZds4TGfDamdy_4Bli6SBLcgKNn39s8KnNtyp16A6D8tqG3tM0f_AVIXnQseweb1bLudcZYpu3KqA1xHUPmiTMRQwk9vVpGsmP2N5RhhsXq93UHYhblXFpB0xYNa9qBEVzY_G5sbURKh9wU-LMi6036HWHiYwJnu7fkON7vo_HvckfSuFYPjq6AX2ZX-CIqc_3U4e06iYECSOvql9IRP2Q',
    'lidc': '\"b=OB85:s=O:r=O:a=O:p=O:g=4997:u=2:x=1:i=1721459833:t=1721513409:v=2:sig=AQFG_Xqua2N61l_esWJ-Hx60gjArtISi\"', 
    'mp_94085d51c4102efbb82a71d85705cdcf_mixpanel': '%7B%22distinct_id%22%3A%20%22cly0fsoa0001r8vrf6ohxiejz%22%2C%22%24device_id%22%3A%20%22190c4a5d0a164d-0b07044bf16257-19525637-13c680-190c4a5d0a2264e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22cly0fsoa0001r8vrf6ohxiejz%22%2C%22%24search_engine%22%3A%20%22google%22%7D'
}
 
cookies = {
    'li_rm': 'AQGnT_vOShf6mQAAAZDEmU1hvMVd-yXN9erF72SOexAa0PlQWYvf-DoFWeMLwUHsupas56wKJZ9_TDExC6MPzD5bezqggRAIxgP15YsdddnD8Juk0fEyK0gG',
    'bcookie': "v=2&d4e6377b-5e2c-435c-8139-bfbc35d5e003",
    'bscookie': "v=1&20240718064819ab5eb69f-d3f0-405c-8e7e-44b05875965fAQGZ4qc3m5ueiYkGLKBBpLLFSj8CHmT7",
    '_gcl_au': '1.1.2023255331.1721285309',
    'aam_uuid': '52479637811493782440203935766855706017',
    'timezone': 'America/Los_Angeles',
    'li_theme': 'light',
    'li_theme_set': 'app',
    '_guid': '5fe5b491-c7a3-41f9-88bd-78e47c02ef3f',
    'li_sugr': 'a8977d7f-1ca8-4841-bb42-2444977ec364',
    'dfpfpt': 'ba4e89be8a044015af4d54f796800e27',
    's_fid': '0D12675185D8A2E6-04A39519A2BAFBAC',
    'visit': 'v=1&M',
    'gpv_pn': 'developer.linkedin.com%2F',
    's_tslv': '1721458194766',
    'mbox': 'PC#8a45615ac753415296ef9be8db9783d9.35_0#1737010196|session#179076dfe8b647c7a7dc2126f5d18031#1721460056', 
    's_ips': '814',
    's_tp': '3026',
    '__cf_bm': '.fU8UxZU_2tvhKxvG9Ec.XK82rGB_wBAV6e1vJ5YJas-1721546258-1.0.1.1-wrwX84DxSWZczhcFZfcNnI920Rla7fcNvKn0q.lfGd0TVl5YHJ_YBpGN.CrmptymrSJwA2brfWbKIPbt5d6aRw',
    'g_state': '{\"i_l\":1,\"i_p\":1721553576999}',
    'chp_token': 'AgHr5fkUNDwscQAAAZDUKa_67scP9yEGLmzZCW6RUpSfr7fLsM6c-n_4D_xRj4Kzl9eDg_h5mzwtcqWs6Idf4ZpZSrnidOvgyDxIUQ',
    'fid': 'AQElzdiS7wqqQQAAAZDULyCWAVTHH2CiQdFjBesub3Gm1sm3a9vrZjyfBBYS02PrZLj2Yb62GqXMeg',
    'fcookie': 'AQHjrKhG2oXMXgAAAZDUMCqE1NZA72FV6DjQMANdU31QRKr14lzbXeUmAP0oR6z0Lee4gpBbzJr5pfj-6VP6MQRrtIpXhUM3XCZIsa7ev8LoW8idCO5zLPzg9r2WdYAEyZv1r_7evcWCkGDxkSPGxI6y1bGbwDznQDp_q2MspEcUuje_Mp1uzPGk-NYDHFqdIPk1S1D6CGfnotvGNgVYPS7yMlnmAkz5Ka1WVoJyGJbqKOp68QwR7CS3aQIcW25WZA443SN86qFbiLC45T15A006ioR879LsdbWzqv3kShmG5ucZaija/qI/i11zIQXzTyZI8MV9SZHhJYaw==',
    'li_at': 'AQEDAVDu5lAAahWOAAABkNQwMY4AAAGQ-Dy1jk4APfc3oYM4ATImdDk22bDCxgz6qaOxBbTD1l-Aa5ngHzrzS93SZmLmfOOhr-0VaWW5nKOGHDHWiwcgR4j3Yj_20xefs4GrCBUIZ286YzwN55fnWOKb',
    'liap': 'true',
    'AnalyticsSyncHistory': 'AQI078n5ZDv33gAAAZDUMDfwCYtFSCY_jkogSNBuXonHEqfVn1m_GgtjPH184d_Oyk6F8aO2JHcCfthAmzoe8A',
    'lms_ads': 'AQEXzWitNiOafAAAAZDUMDi4J07QxFR3VmgavYcEgJ4mi2lvrqgenzNztoDM5SlEsDM_6115TuWkC_DT6K_WTNtsE9iJH7-h',
    'lms_analytics': 'AQEXzWitNiOafAAAAZDUMDi4J07QxFR3VmgavYcEgJ4mi2lvrqgenzNztoDM5SlEsDM_6115TuWkC_DT6K_WTNtsE9iJH7-h; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19926%7CMCMID%7C51959362510172131990151901119295821418%7CMCAAMLH-1722151649%7C7%7CMCAAMB-1722151649%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1721554049s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1269007817',
    'JSESSIONID': '\"ajax:2095855091259253565\"',
    'lang': 'v=2&lang=en-us',
    'sdsc': '33%3A1%2C1721546945845%7EJBSK%2C0%7EJOBS%2C67156wBKM9lgFp1ESoklF71lmLA3XUFc%3D', 
    'UserMatchHistory': 'AQIlhLpQwCOimgAAAZDUNei2m53kK3_mQaQAwmDUGmCrI86THJXJjY_8rpJ8DffD-4CmI4MYxshftlinRGd198oX5AWtjERcVJc96weXUDtLzAi7Y6Kfh8Y_fGiBJ8oPnzMcXiWl_utK5qRMKR7wssLtx5oj_awXNv6_AKsyO-5bozGuxUkv0bPX8xkD-MQYq1UXSXtRNDuypSy7qGyZTLS-YuuRj9BESDwIYnr1qowSIz8V5abxLCquGgkC8_X8mpzHiD6cJTj_3r3Nyd0D-oDDdwdsdyqzANPbKdkBbDM7vnFidTFvGsoyVzc2xIe8uQ9YJXzRo55-H8WIsY9LU7zkpQcTha_uSdKMqfIPWng7OHYfhQ; mp_94085d51c4102efbb82a71d85705cdcf_mixpanel=%7B%22distinct_id%22%3A%20%22cly0fsoa0001r8vrf6ohxiejz%22%2C%22%24device_id%22%3A%20%22190c4a5d0a164d-0b07044bf16257-19525637-13c680-190c4a5d0a2264e%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%22cly0fsoa0001r8vrf6ohxiejz%22%2C%22%24search_engine%22%3A%20%22google%22%7D',
    'lidc': '\"b=TB08:s=T:r=T:a=T:p=T:g=5559:u=1:x=1:i=1721547221:t=1721633247:v=2:sig=AQHbhdseDoAiYCrSMoeb_OXGDKqDCM0y\"', 
    'fptctx2': 'taBcrIH61PuCVH7eNCyH0FFaWZWIHTJWSYlBtG47cVuNNpuPAG73YpdQnHAjkKbs3ERY%252bG3rQRxhKRbE6NbkkdSU2%252f8XHuf1SUmiJY4ai%252bySMyOT6fILonpyazELaQM8fG33K%252bZQgL6VGY0XqKXrHSQm%252bEzk9AyrvD4FouJ9keh5KToaBiPAzWZ5SWMZcP0yzZ%252bH5wI7cCrbodWfvPQqw51ZaBQZdBIseacwbpUBBFOuyR5%252fL8ngwwp0qGP%252fJE0H4To2LmKGHcJcGaE2c8fcZHxYU5K6ubxTv3Kz0yqOUkS%252byOxvc8o%252fpg4qy3w3mFQLTG%252fJOWSq5xn6qyNTQBqZyahVPitd%252fNp2OrYsrGd%252fDx0%253d'
}

def get_url():
    url = (
        f'https://www.linkedin.com/voyager/api/graphql?variables=(start:0,query:('
        f'flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,queryParameters:List((key:cardType,value:List(SAVED)))))'
        f'&queryId=voyagerSearchDashClusters.ff737c692102a8ce842be8f129f834ae'
    )
    return url
 
 
def find_jobs():    
    url = get_url()
    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200:
        return {
            "error": "Response status code is not 200 for /voyager/api/graphql",
            "response": response
        }
    
    # print(response.json())
    return response.json()

def parse_jobs_response(responseJson):
    # jobs = responseJson['data']['data']['data']['searchDashClustersByAll']['elements']['items']
    # jobs = responseJson['data']['data']['searchDashClustersByAll']['elements']['0']['items']
    print(responseJson)
    jobs = responseJson['data']['data']['searchDashClustersByAll']['elements'][0]['items']


    def extract_job_id(job_id_string):
        # urn:li:fsd_entityResultViewModel:(urn:li:fsd_jobPosting:3974986581,SEARCH_MY_ITEMS_JOB_SEEKER,DEFAULT)
        parts = job_id_string.split(':')
        number = parts[-1].split(',')[0]
        return number

    job_ids = []
    for job in jobs:
        job_id = extract_job_id(job['item']['*entityResult'])
        job_ids.append(job_id)
    print(job_ids)

    return job_ids

def create_job_urls(job_ids):
    job_urls = []
    base_url = 'https://www.linkedin.com/jobs/view/'
    print(job_ids)
    for job_id in job_ids:
        job_url = base_url + job_id
        job_urls.append(job_url)
    return job_urls

def fetch_job_urls():
    response_json = find_jobs()
    job_ids = parse_jobs_response(response_json)
    job_urls = create_job_urls(job_ids)
    return job_urls

if __name__ == '__main__':
    response_json = find_jobs()
    job_ids = parse_jobs_response(response_json)
    job_urls = create_job_urls(job_ids)
    print(job_urls)
