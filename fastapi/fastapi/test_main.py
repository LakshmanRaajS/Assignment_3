from fastapi.testclient import TestClient
from main import app
import boto3
import os

client = TestClient(app)

# Test login_for_access_token
def test_login_for_access_token():
    response = client.post(
        url = "/token",
        json = {"username": "damg7245", "password": "spring2023"}
    )
    assert response.status_code == 200


def test_fetch_url():
    response = client.post(
        url = "/fetch_url",
        json = {
            'year': 2022,
            'month': 2,
            'date': 6,
            'station': 'KABR'
            }
        )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == 'https://noaa-nexrad-level2.s3.amazonaws.com/index.html#2022/02/06/KABR'

#Tests the nexrad year list returned
def test_list_years_nexrad():
    response = client.get("/list-years-nexrad")
    assert response.status_code == 200
    message = response.json()["year_list"]
    assert message == ['2023', '2022']

#Tests the nexrad month list of a particular year
def test_list_months_nexrad():
    response = client.post(
        url = "/list-months-nexrad?year=2023",
    )
    assert response.status_code == 200
    message = response.json()["month_list"]
    assert message == ['02', '01']

#Tests the nexrad days returned for particular year and month
def test_list_days_nexrad():
    response = client.post(
        url = "/list-days-nexrad?year=2023&month=01"
        )
    assert response.status_code == 200
    message = response.json()["days_list"]
    assert message == [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31"
    ]

#Tests for the nexrad stations returned for a particular year month day
def test_list_stations_nexrad():
    response = client.post(
        url = "/list-stations-nexrad?year=2023&month=01&day=01"
    )
    assert response.status_code == 200
    message = response.json()["stations_list"]
    assert message == [
        "FOP1",
        "KABR",
        "KABX",
        "KAKQ",
        "KAMA",
        "KAMX",
        "KAPX",
        "KARX",
        "KATX",
        "KBBX",
        "KBGM",
        "KBHX",
        "KBIS",
        "KBLX",
        "KBMX",
        "KBOX",
        "KBRO",
        "KBUF",
        "KBYX",
        "KCAE",
        "KCBW",
        "KCBX",
        "KCCX",
        "KCLE",
        "KCLX",
        "KCRP",
        "KCXX",
        "KCYS",
        "KDAX",
        "KDDC",
        "KDFX",
        "KDGX",
        "KDIX",
        "KDLH",
        "KDMX",
        "KDOX",
        "KDTX",
        "KDVN",
        "KDYX",
        "KEAX",
        "KEMX",
        "KENX",
        "KEOX",
        "KEPZ",
        "KESX",
        "KEVX",
        "KEWX",
        "KEYX",
        "KFCX",
        "KFDR",
        "KFDX",
        "KFFC",
        "KFSD",
        "KFSX",
        "KFTG",
        "KFWS",
        "KGGW",
        "KGJX",
        "KGLD",
        "KGRB",
        "KGRK",
        "KGRR",
        "KGWX",
        "KGYX",
        "KHDX",
        "KHGX",
        "KHNX",
        "KHTX",
        "KICT",
        "KICX",
        "KILN",
        "KILX",
        "KIND",
        "KINX",
        "KIWA",
        "KIWX",
        "KJAX",
        "KJGX",
        "KJKL",
        "KLBB",
        "KLCH",
        "KLGX",
        "KLIX",
        "KLNX",
        "KLOT",
        "KLRX",
        "KLSX",
        "KLTX",
        "KLVX",
        "KLWX",
        "KLZK",
        "KMAF",
        "KMAX",
        "KMBX",
        "KMHX",
        "KMKX",
        "KMLB",
        "KMOB",
        "KMPX",
        "KMQT",
        "KMRX",
        "KMSX",
        "KMTX",
        "KMUX",
        "KMVX",
        "KMXX",
        "KNKX",
        "KNQA",
        "KOAX",
        "KOHX",
        "KOKX",
        "KOTX",
        "KPAH",
        "KPBZ",
        "KPDT",
        "KPOE",
        "KPUX",
        "KRAX",
        "KRGX",
        "KRIW",
        "KRLX",
        "KRTX",
        "KSFX",
        "KSGF",
        "KSHV",
        "KSJT",
        "KSOX",
        "KSRX",
        "KTBW",
        "KTFX",
        "KTLH",
        "KTLX",
        "KTWX",
        "KTYX",
        "KUDX",
        "KUEX",
        "KVAX",
        "KVBX",
        "KVNX",
        "KVTX",
        "KVWX",
        "KYUX",
        "PACG",
        "PAEC",
        "PAHG",
        "PAKC",
        "PAPD",
        "PGUA",
        "PHKI",
        "PHKM",
        "PHMO",
        "PHWA",
        "RKJK",
        "RODN",
        "TADW",
        "TATL",
        "TBNA",
        "TBOS",
        "TBWI",
        "TCLT",
        "TCMH",
        "TCVG",
        "TDAL",
        "TDAY",
        "TDCA",
        "TDEN",
        "TDTW",
        "TEWR",
        "TFLL",
        "THOU",
        "TIAD",
        "TIAH",
        "TICH",
        "TIDS",
        "TJFK",
        "TJUA",
        "TLAS",
        "TLVE",
        "TMCI",
        "TMCO",
        "TMDW",
        "TMEM",
        "TMIA",
        "TMKE",
        "TMSP",
        "TMSY",
        "TOKC",
        "TORD",
        "TPHL",
        "TPHX",
        "TPIT",
        "TRDU",
        "TSDF",
        "TSJU",
        "TSLC",
        "TSTL",
        "TTPA",
        "TTUL"
    ]

#test for the nexrad files returned for a particular year month day and station
def test_list_files_nexrad():
    response = client.post(
        url = "/list-files-nexrad?year=2023&month=01&day=01&station=KABR"
    )
    assert response.status_code == 200
    message = response.json()["file_list"]
    assert message == [
        "KABR20230101_000142_V06",
        "KABR20230101_000825_V06",
        "KABR20230101_001508_V06",
        "KABR20230101_002151_V06",
        "KABR20230101_002834_V06",
        "KABR20230101_003517_V06",
        "KABR20230101_004201_V06",
        "KABR20230101_004949_V06",
        "KABR20230101_005634_V06",
        "KABR20230101_005634_V06_MDM",
        "KABR20230101_010318_V06",
        "KABR20230101_011002_V06",
        "KABR20230101_011645_V06",
        "KABR20230101_012327_V06",
        "KABR20230101_013012_V06",
        "KABR20230101_013656_V06",
        "KABR20230101_014339_V06",
        "KABR20230101_015023_V06",
        "KABR20230101_015706_V06",
        "KABR20230101_015706_V06_MDM",
        "KABR20230101_020349_V06",
        "KABR20230101_021033_V06",
        "KABR20230101_021715_V06",
        "KABR20230101_022359_V06",
        "KABR20230101_023042_V06",
        "KABR20230101_023725_V06",
        "KABR20230101_024407_V06",
        "KABR20230101_025050_V06",
        "KABR20230101_025734_V06",
        "KABR20230101_025734_V06_MDM",
        "KABR20230101_030426_V06",
        "KABR20230101_031119_V06",
        "KABR20230101_031806_V06",
        "KABR20230101_032449_V06",
        "KABR20230101_033133_V06",
        "KABR20230101_033816_V06",
        "KABR20230101_034504_V06",
        "KABR20230101_035150_V06",
        "KABR20230101_035841_V06",
        "KABR20230101_035841_V06_MDM",
        "KABR20230101_040537_V06",
        "KABR20230101_041220_V06",
        "KABR20230101_041922_V06",
        "KABR20230101_042626_V06",
        "KABR20230101_043329_V06",
        "KABR20230101_044025_V06",
        "KABR20230101_044727_V06",
        "KABR20230101_045415_V06",
        "KABR20230101_045415_V06_MDM",
        "KABR20230101_050107_V06",
        "KABR20230101_050809_V06",
        "KABR20230101_051455_V06",
        "KABR20230101_052147_V06",
        "KABR20230101_052835_V06",
        "KABR20230101_053523_V06",
        "KABR20230101_054210_V06",
        "KABR20230101_054906_V06",
        "KABR20230101_055553_V06",
        "KABR20230101_055553_V06_MDM",
        "KABR20230101_060241_V06",
        "KABR20230101_060939_V06",
        "KABR20230101_061626_V06",
        "KABR20230101_062323_V06",
        "KABR20230101_063026_V06",
        "KABR20230101_063723_V06",
        "KABR20230101_064426_V06",
        "KABR20230101_065122_V06",
        "KABR20230101_065818_V06",
        "KABR20230101_065818_V06_MDM",
        "KABR20230101_070514_V06",
        "KABR20230101_071209_V06",
        "KABR20230101_071912_V06",
        "KABR20230101_072603_V06",
        "KABR20230101_073301_V06",
        "KABR20230101_073958_V06",
        "KABR20230101_074701_V06",
        "KABR20230101_075356_V06",
        "KABR20230101_075356_V06_MDM",
        "KABR20230101_080053_V06",
        "KABR20230101_080750_V06",
        "KABR20230101_081445_V06",
        "KABR20230101_082141_V06",
        "KABR20230101_082838_V06",
        "KABR20230101_083530_V06",
        "KABR20230101_084226_V06",
        "KABR20230101_085030_V06",
        "KABR20230101_085721_V06",
        "KABR20230101_085721_V06_MDM",
        "KABR20230101_090419_V06",
        "KABR20230101_091112_V06",
        "KABR20230101_091803_V06",
        "KABR20230101_092455_V06",
        "KABR20230101_093144_V06",
        "KABR20230101_093833_V06",
        "KABR20230101_094520_V06",
        "KABR20230101_095218_V06",
        "KABR20230101_095907_V06",
        "KABR20230101_095907_V06_MDM",
        "KABR20230101_100555_V06",
        "KABR20230101_101242_V06",
        "KABR20230101_101925_V06",
        "KABR20230101_102610_V06",
        "KABR20230101_103254_V06",
        "KABR20230101_103939_V06",
        "KABR20230101_104623_V06",
        "KABR20230101_105307_V06",
        "KABR20230101_105952_V06",
        "KABR20230101_105952_V06_MDM",
        "KABR20230101_110635_V06",
        "KABR20230101_111319_V06",
        "KABR20230101_112002_V06",
        "KABR20230101_112646_V06",
        "KABR20230101_113331_V06",
        "KABR20230101_114020_V06",
        "KABR20230101_114709_V06",
        "KABR20230101_115356_V06",
        "KABR20230101_115356_V06_MDM",
        "KABR20230101_120039_V06",
        "KABR20230101_120723_V06",
        "KABR20230101_121407_V06",
        "KABR20230101_122050_V06",
        "KABR20230101_122734_V06",
        "KABR20230101_123418_V06",
        "KABR20230101_124102_V06",
        "KABR20230101_124747_V06",
        "KABR20230101_125430_V06",
        "KABR20230101_125430_V06_MDM",
        "KABR20230101_130114_V06",
        "KABR20230101_130757_V06",
        "KABR20230101_131442_V06",
        "KABR20230101_132124_V06",
        "KABR20230101_132809_V06",
        "KABR20230101_133457_V06",
        "KABR20230101_134141_V06",
        "KABR20230101_134824_V06",
        "KABR20230101_135508_V06",
        "KABR20230101_135508_V06_MDM",
        "KABR20230101_140152_V06",
        "KABR20230101_140837_V06",
        "KABR20230101_141522_V06",
        "KABR20230101_142205_V06",
        "KABR20230101_142849_V06",
        "KABR20230101_143532_V06",
        "KABR20230101_144217_V06",
        "KABR20230101_144900_V06",
        "KABR20230101_145552_V06",
        "KABR20230101_145552_V06_MDM",
        "KABR20230101_150236_V06",
        "KABR20230101_150924_V06",
        "KABR20230101_151608_V06",
        "KABR20230101_152252_V06",
        "KABR20230101_152937_V06",
        "KABR20230101_153621_V06",
        "KABR20230101_154305_V06",
        "KABR20230101_154949_V06",
        "KABR20230101_155637_V06",
        "KABR20230101_155637_V06_MDM",
        "KABR20230101_160325_V06",
        "KABR20230101_161010_V06",
        "KABR20230101_161653_V06",
        "KABR20230101_162337_V06",
        "KABR20230101_163021_V06",
        "KABR20230101_163705_V06",
        "KABR20230101_164350_V06",
        "KABR20230101_165145_V06",
        "KABR20230101_165827_V06",
        "KABR20230101_165827_V06_MDM",
        "KABR20230101_170520_V06",
        "KABR20230101_171209_V06",
        "KABR20230101_171857_V06",
        "KABR20230101_172544_V06",
        "KABR20230101_173233_V06",
        "KABR20230101_173922_V06",
        "KABR20230101_174606_V06",
        "KABR20230101_175249_V06",
        "KABR20230101_175934_V06",
        "KABR20230101_175934_V06_MDM",
        "KABR20230101_180618_V06",
        "KABR20230101_181302_V06",
        "KABR20230101_181946_V06",
        "KABR20230101_182629_V06",
        "KABR20230101_183313_V06",
        "KABR20230101_184001_V06",
        "KABR20230101_184650_V06",
        "KABR20230101_185337_V06",
        "KABR20230101_185337_V06_MDM",
        "KABR20230101_190021_V06",
        "KABR20230101_190709_V06",
        "KABR20230101_191357_V06",
        "KABR20230101_192045_V06",
        "KABR20230101_192732_V06",
        "KABR20230101_193420_V06",
        "KABR20230101_194108_V06",
        "KABR20230101_194756_V06",
        "KABR20230101_195448_V06",
        "KABR20230101_195448_V06_MDM",
        "KABR20230101_200133_V06",
        "KABR20230101_200817_V06",
        "KABR20230101_201501_V06",
        "KABR20230101_202144_V06",
        "KABR20230101_202828_V06",
        "KABR20230101_203513_V06",
        "KABR20230101_204157_V06",
        "KABR20230101_204841_V06",
        "KABR20230101_205526_V06",
        "KABR20230101_205526_V06_MDM",
        "KABR20230101_210210_V06",
        "KABR20230101_210854_V06",
        "KABR20230101_211537_V06",
        "KABR20230101_212221_V06",
        "KABR20230101_212904_V06",
        "KABR20230101_213548_V06",
        "KABR20230101_214233_V06",
        "KABR20230101_214917_V06",
        "KABR20230101_215601_V06",
        "KABR20230101_215601_V06_MDM",
        "KABR20230101_220250_V06",
        "KABR20230101_220935_V06",
        "KABR20230101_221618_V06",
        "KABR20230101_222307_V06",
        "KABR20230101_222952_V06",
        "KABR20230101_223636_V06",
        "KABR20230101_224338_V06",
        "KABR20230101_225022_V06",
        "KABR20230101_225706_V06",
        "KABR20230101_225706_V06_MDM",
        "KABR20230101_230350_V06",
        "KABR20230101_231034_V06",
        "KABR20230101_231724_V06",
        "KABR20230101_232407_V06",
        "KABR20230101_233056_V06",
        "KABR20230101_233744_V06",
        "KABR20230101_234426_V06",
        "KABR20230101_235109_V06",
        "KABR20230101_235757_V06",
        "KABR20230101_235757_V06_MDM"
    ]

#Test the url return function
def test_fetch_url_nexrad():
    response = client.post(
        url = "/fetch-url-nexrad?name=KABR20230101_000142_V06"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://damg-test.s3.amazonaws.com/logs/nexrad/KABR20230101_000142_V06"

#Test for proper function of url validation
def test_validate_url_nexrad():
    response = client.post(
        url = "/validate-url-nexrad?name=%22https%3A%2F%2Fdamg-test.s3.amazonaws.com%2Flogs%2Fnexrad%2FKABR20230101_000142_V06%22"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://noaa-nexrad-level2.s3.amazonaws.com/ps%3A///d/am/%22htt/%22https%3A//damg-test.s3.amazonaws.com/logs/nexrad/KABR20230101_000142_V06%22"


#Tests the goes year list returned
def test_list_years_goes():
    response = client.get("/list-years-goes")
    assert response.status_code == 200
    message = response.json()["year_list"]
    assert message == ["2022","2023"]

#Tests the goes days list of a particular year
def test_list_days_goes():
    response = client.post(
        url = "/list-days-goes?year=2023"
    )
    assert response.status_code == 200
    message = response.json()["days_list"]
    assert message == [
        "001",
        "002",
        "003",
        "004",
        "005",
        "006",
        "007",
        "008",
        "009",
        "010",
        "011",
        "012",
        "013",
        "014",
        "015",
        "016",
        "017",
        "018",
        "019",
        "020",
        "021",
        "022",
        "023",
        "024",
        "025",
        "026",
        "027",
        "028",
        "029",
        "030",
        "031",
        "032",
        "033",
        "034",
        "035",
        "036",
        "037",
        "038",
        "039",
        "040",
        "041",
        "042",
        "043",
        "044",
        "045",
        "046",
        "047",
        "048",
        "049",
        "050",
        "051",
        "052",
        "053",
        "054",
        "055",
    ]

#Tests the goes hours list of a particular year and day
def test_list_hours_goes():
    response = client.post(
        url = "/list-hours-goes?year=2023&day=001"
    )
    assert response.status_code == 200
    message = response.json()["hours_list"]
    assert message == [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23"
    ]

#Tests the goes files list of a particular year day and hour
def test_files_goes():
    response = client.post(
        url = "/list-files-goes?year=2023&day=001&hour=00"
    )
    assert response.status_code == 200
    message = response.json()["file_list"]
    assert message == [
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010006170_e20230010008548_c20230010008589.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010011170_e20230010013546_c20230010013581.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010016170_e20230010018545_c20230010018590.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010021170_e20230010023548_c20230010023586.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010026170_e20230010028549_c20230010029007.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010031170_e20230010033544_c20230010034008.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010036170_e20230010038545_c20230010038583.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010041170_e20230010043546_c20230010043579.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010046170_e20230010048544_c20230010048590.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010051170_e20230010053545_c20230010053588.nc",
        "OR_ABI-L1b-RadC-M6C01_G18_s20230010056170_e20230010058547_c20230010058582.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010001170_e20230010003545_c20230010003578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010006170_e20230010008545_c20230010008578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010011170_e20230010013543_c20230010013578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010016170_e20230010018543_c20230010018578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010021170_e20230010023545_c20230010023577.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010026170_e20230010028543_c20230010028575.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010031170_e20230010033543_c20230010033577.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010036170_e20230010038545_c20230010038578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010041170_e20230010043543_c20230010043576.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010046170_e20230010048544_c20230010048578.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010051170_e20230010053543_c20230010053577.nc",
        "OR_ABI-L1b-RadC-M6C02_G18_s20230010056170_e20230010058545_c20230010058576.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010001170_e20230010003544_c20230010003590.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010006170_e20230010008545_c20230010008583.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010011170_e20230010013546_c20230010014002.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010016170_e20230010018545_c20230010018587.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010021170_e20230010023547_c20230010023581.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010026170_e20230010028547_c20230010028580.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010031170_e20230010033545_c20230010033586.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010036170_e20230010038547_c20230010038588.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010041170_e20230010043545_c20230010043595.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010046170_e20230010048545_c20230010048593.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010051170_e20230010053545_c20230010053584.nc",
        "OR_ABI-L1b-RadC-M6C03_G18_s20230010056170_e20230010058545_c20230010058585.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010001170_e20230010003543_c20230010004021.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010006170_e20230010008543_c20230010009018.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010011170_e20230010013543_c20230010013589.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010016170_e20230010018543_c20230010018593.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010021170_e20230010023543_c20230010024009.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010026170_e20230010028543_c20230010028585.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010031170_e20230010033543_c20230010034024.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010036170_e20230010038543_c20230010039001.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010041170_e20230010043543_c20230010043587.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010046170_e20230010048543_c20230010048585.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010051170_e20230010053543_c20230010053593.nc",
        "OR_ABI-L1b-RadC-M6C04_G18_s20230010056170_e20230010058543_c20230010058590.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010001170_e20230010003545_c20230010004033.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010006170_e20230010008546_c20230010009031.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010011170_e20230010013544_c20230010014031.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010016170_e20230010018544_c20230010019008.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010021170_e20230010023545_c20230010024028.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010026170_e20230010028548_c20230010029012.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010031170_e20230010033545_c20230010034030.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010036170_e20230010038547_c20230010039022.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010041170_e20230010043544_c20230010044021.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010046170_e20230010048547_c20230010049037.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010051170_e20230010053546_c20230010054018.nc",
        "OR_ABI-L1b-RadC-M6C05_G18_s20230010056170_e20230010058547_c20230010059020.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010001170_e20230010003550_c20230010004042.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010006170_e20230010008550_c20230010009025.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010011170_e20230010013549_c20230010014038.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010016170_e20230010018549_c20230010019029.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010021170_e20230010023549_c20230010024030.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010026170_e20230010028549_c20230010028588.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010031170_e20230010033549_c20230010034003.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010036170_e20230010038549_c20230010039004.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010041170_e20230010043549_c20230010043591.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010046170_e20230010048549_c20230010049039.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010051170_e20230010053550_c20230010053580.nc",
        "OR_ABI-L1b-RadC-M6C06_G18_s20230010056170_e20230010058551_c20230010058594.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010001170_e20230010003556_c20230010003594.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010006170_e20230010008556_c20230010008591.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010011170_e20230010013555_c20230010013592.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010016170_e20230010018555_c20230010019005.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010021170_e20230010023555_c20230010024037.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010026170_e20230010028556_c20230010028591.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010031170_e20230010033555_c20230010034027.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010036170_e20230010038555_c20230010039019.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010041170_e20230010043557_c20230010044002.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010046170_e20230010048556_c20230010049013.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010051170_e20230010053555_c20230010054003.nc",
        "OR_ABI-L1b-RadC-M6C07_G18_s20230010056170_e20230010058557_c20230010058597.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010001170_e20230010003543_c20230010004004.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010006170_e20230010008543_c20230010009038.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010011170_e20230010013543_c20230010014033.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010016170_e20230010018543_c20230010019010.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010021170_e20230010023543_c20230010024005.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010026170_e20230010028543_c20230010029026.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010031170_e20230010033543_c20230010034014.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010036170_e20230010038543_c20230010039009.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010041170_e20230010043543_c20230010044038.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010046170_e20230010048543_c20230010049034.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010051170_e20230010053543_c20230010054029.nc",
        "OR_ABI-L1b-RadC-M6C08_G18_s20230010056170_e20230010058543_c20230010059035.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010001170_e20230010003550_c20230010004036.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010006170_e20230010008549_c20230010008594.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010011170_e20230010013550_c20230010014029.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010016170_e20230010018549_c20230010019002.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010021170_e20230010023549_c20230010024032.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010026170_e20230010028551_c20230010028598.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010031170_e20230010033550_c20230010034020.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010036170_e20230010038549_c20230010039013.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010041170_e20230010043549_c20230010044010.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010046170_e20230010048550_c20230010049023.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010051170_e20230010053551_c20230010053599.nc",
        "OR_ABI-L1b-RadC-M6C09_G18_s20230010056170_e20230010058549_c20230010059023.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010001170_e20230010003556_c20230010003599.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010006170_e20230010008555_c20230010008598.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010011170_e20230010013557_c20230010014005.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010016170_e20230010018555_c20230010019020.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010021170_e20230010023556_c20230010023589.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010026170_e20230010028557_c20230010029020.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010031170_e20230010033556_c20230010033596.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010036170_e20230010038554_c20230010039028.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010041170_e20230010043555_c20230010044017.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010046170_e20230010048555_c20230010049001.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010051170_e20230010053557_c20230010054011.nc",
        "OR_ABI-L1b-RadC-M6C10_G18_s20230010056170_e20230010058555_c20230010059026.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010001170_e20230010003543_c20230010004002.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010006170_e20230010008543_c20230010009000.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010011170_e20230010013543_c20230010014017.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010016170_e20230010018543_c20230010018595.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010021170_e20230010023543_c20230010024015.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010026170_e20230010028543_c20230010029001.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010031170_e20230010033543_c20230010033594.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010036170_e20230010038543_c20230010038591.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010041170_e20230010043543_c20230010043597.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010046170_e20230010048543_c20230010048599.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010051170_e20230010053543_c20230010053590.nc",
        "OR_ABI-L1b-RadC-M6C11_G18_s20230010056170_e20230010058543_c20230010059001.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010001170_e20230010003550_c20230010004030.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010006170_e20230010008550_c20230010009035.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010011170_e20230010013549_c20230010014020.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010016170_e20230010018549_c20230010019000.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010021170_e20230010023549_c20230010023591.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010026170_e20230010028549_c20230010029003.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010031170_e20230010033550_c20230010033591.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010036170_e20230010038550_c20230010038593.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010041170_e20230010043549_c20230010044024.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010046170_e20230010048551_c20230010049042.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010051170_e20230010053549_c20230010053596.nc",
        "OR_ABI-L1b-RadC-M6C12_G18_s20230010056170_e20230010058549_c20230010059012.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010001170_e20230010003556_c20230010004012.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010006170_e20230010008556_c20230010009001.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010011170_e20230010013555_c20230010013596.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010016170_e20230010018555_c20230010018598.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010021170_e20230010023556_c20230010024021.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010026170_e20230010028556_c20230010028595.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010031170_e20230010033555_c20230010033598.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010036170_e20230010038555_c20230010038599.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010041170_e20230010043555_c20230010044005.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010046170_e20230010048557_c20230010049004.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010051170_e20230010053557_c20230010054005.nc",
        "OR_ABI-L1b-RadC-M6C13_G18_s20230010056170_e20230010058559_c20230010059028.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010001170_e20230010003543_c20230010004025.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010006170_e20230010008543_c20230010009004.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010011170_e20230010013543_c20230010014010.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010016170_e20230010018543_c20230010019017.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010021170_e20230010023543_c20230010023597.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010026170_e20230010028543_c20230010029017.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010031170_e20230010033543_c20230010034032.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010036170_e20230010038543_c20230010038598.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010041170_e20230010043543_c20230010044030.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010046170_e20230010048543_c20230010049030.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010051170_e20230010053543_c20230010054022.nc",
        "OR_ABI-L1b-RadC-M6C14_G18_s20230010056170_e20230010058543_c20230010059005.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010001170_e20230010003549_c20230010004038.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010006170_e20230010008549_c20230010009014.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010011170_e20230010013549_c20230010014036.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010016170_e20230010018551_c20230010019026.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010021170_e20230010023549_c20230010024046.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010026170_e20230010028549_c20230010029028.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010031170_e20230010033549_c20230010034036.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010036170_e20230010038551_c20230010039034.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010041170_e20230010043549_c20230010044026.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010046170_e20230010048549_c20230010049020.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010051170_e20230010053549_c20230010054008.nc",
        "OR_ABI-L1b-RadC-M6C15_G18_s20230010056170_e20230010058550_c20230010059031.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010001170_e20230010003555_c20230010004028.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010006170_e20230010008555_c20230010009028.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010011170_e20230010013557_c20230010014026.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010016170_e20230010018557_c20230010019023.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010021170_e20230010023555_c20230010024039.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010026170_e20230010028556_c20230010029023.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010031170_e20230010033555_c20230010034010.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010036170_e20230010038561_c20230010039026.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010041170_e20230010043555_c20230010044033.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010046170_e20230010048557_c20230010048597.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010051170_e20230010053556_c20230010054000.nc",
        "OR_ABI-L1b-RadC-M6C16_G18_s20230010056170_e20230010058556_c20230010059037.nc"
    ]

#Tests the goes files list of a particular year day and hour
def test_fetch_url_goes():
    response = client.post(
        url = "/fetch-url-goes?name=OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://damg-test.s3.amazonaws.com/logs/goes18/OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc"

#Tests the validate url goes function
def test_validate_url_goes():
    response = client.post(
        url = "/validate-url-goes?name=%22https%3A%2F%2Fdamg-test.s3.amazonaws.com%2Flogs%2Fgoes18%2FOR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc%22"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://noaa-goes18.s3.amazonaws.com/ABI-L1b-RadC/%3A//d/amg/-t/%22https%3A//damg-test.s3.amazonaws.com/logs/goes18/OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc%22"

#Tests fetch_url_goes_from_name
def test_fetch_url_goes_from_name():
    response = client.post(
        url = "/fetch-url-goes-from-name?name=OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://damg-test.s3.amazonaws.com/logs/goes18/OR_ABI-L1b-RadC-M6C01_G18_s20230010001170_e20230010003544_c20230010003582.nc"


#Tests fetch_url_nexrad_from_name
def test_fetch_url_nexrad_from_name():
    response = client.post(
        url = "/fetch-url-nexrad-from-name?name=KABR20230101_000142_V06"
    )
    assert response.status_code == 200
    message = response.json()["url"]
    assert message == "https://damg-test.s3.amazonaws.com/logs/nexrad/KABR20230101_000142_V06"

#Tests mapping_stations
def test_mapping_stations():
    response = client.get(
        url = '/mapping-stations'
    )
    assert response.status_code == 200