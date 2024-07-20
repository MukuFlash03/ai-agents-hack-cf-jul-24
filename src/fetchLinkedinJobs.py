'''
https://www.linkedin.com/voyager/api/graphql?
    variables=(
        start:0,
        query:(
            flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,
            queryParameters:List((key:cardType,value:List(SAVED)))
        )
    )&
    queryId=voyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2
'''

import requests

headers = {
    # ":authority": "www.linkedin.com",
    # ":method": "GET",
    # ":path": "/voyager/api/graphql?variables=(start:0,query:(flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,queryParameters:List((key:cardType,value:List(SAVED)))))&queryId=voyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2",
    # ":scheme": "https",
    "Accept": "application/vnd.linkedin.normalized+json+2.1",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    # "Cookie": "[long string of cookies, omitted for brevity]",
    "Csrf-Token": "ajax:5403365271819302899",
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
    "X-Li-Page-Instance": "urn:li:page:d_flagship3_myitems_savedjobs;lURV5NiPSzK4dUROKOBwpw==",
    "X-Li-Pem-Metadata": "Voyager - My Items=myitems-saved-jobs",
    "X-Li-Track": '{\"clientVersion\":\"1.13.20142\",\"mpVersion\":\"1.13.20142\",\"osName\":\"web\",\"timezoneOffset\":-7,\"timezone\":\"America/Los_Angeles\",\"deviceFormFactor\":\"DESKTOP\",\"mpName\":\"voyager-web\",\"displayDensity\":1.600000023841858,\"displayWidth\":2304.0000343322754,\"displayHeight\":1440.0000214576721}',
    "X-Restli-Protocol-Version": "2.0.0"
}


# headers = {
#     'Accept': '*/*',
#     'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,uk;q=0.7',
#     'Cache-Control': 'no-cache',
#     'Connection': 'keep-alive',
#     'Origin': 'https://jobs.lever.co',
#     'Pragma': 'no-cache',
#     'Referer': 'https://jobs.lever.co/attentive/0910dc79-6140-4f60-8669-46da5d5865bd/apply',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
# }

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
    'JSESSIONID': '\"ajax:5403365271819302899\"',
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
 
# cookies = {
#     'cookieyesID': 'N3ZnZ1prcDBOU29ob3lNWTdueFNhS1Exd1VORTJVZVE',
#     '_ga_Q34B1R5W4J': 'GS1.1.1691334905.1.0.1691334906.59.0.0',
#     '__q_state_x1HFACWrNZVeUTqj': 'eyJ1dWlkIjoiYzk0YjFlMTItN2FlNi00NWQwLTg0OTAtN2Y4ZGZmMzEwZTQxIiwiY29va2llRG9tYWluIjoibGV2ZXIuY28iLCJtZXNzZW5nZXJFeHBhbmRlZCI6ZmFsc2UsInByb21wdERpc21pc3NlZCI6ZmFsc2UsImNvbnZlcnNhdGlvbklkIjoiMTE5NjYxMzQ0MDQwNTA3MDI3MCJ9',
#     '_ga': 'GA1.3.464814093.1691425673',
#     '_gid': 'GA1.3.819753513.1691425673',
#     '_ga_T90MF42ZY0': 'GS1.3.1691425672.1.0.1691425672.0.0.0',
#     'lever-referer': 'https%3A%2F%2Fjobs.lever.co%2Fattentive%2F0910dc79-6140-4f60-8669-46da5d5865bd',
# }
 

def get_url():
    url = (
        f'https://www.linkedin.com/voyager/api/graphql?variables=(start:0,query:('
        f'flagshipSearchIntent:SEARCH_MY_ITEMS_JOB_SEEKER,queryParameters:List((key:cardType,value:List(SAVED)))))'
        f'&queryId=voyagerSearchDashClusters.e796818a0b9b74f072bcdb11099b30f2'
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
    jobs = responseJson['data']['data']['searchDashClustersByAll']
    print(jobs)


response_json = find_jobs()
parse_jobs_response(response_json)
