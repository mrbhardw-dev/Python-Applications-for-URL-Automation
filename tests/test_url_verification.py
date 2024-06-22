import os
import pytest
from PACKAGES.url_verification import verify_urls
from PACKAGES.utils import app_root


def test_verify_internal_urls(mocker):
    mocker.patch('PACKAGES.url_verification.convert_to_csv')
    mocker.patch('PACKAGES.url_verification.lookup_dns')
    mocker.patch('PACKAGES.url_verification.dns_clean')
    mocker.patch('PACKAGES.url_verification.url_convert')
    mocker.patch('PACKAGES.url_verification.format_report')
    mocker.patch('PACKAGES.url_verification.generate_report')
    
    verify_urls('internal')
    
    assert os.path.exists(f"{app_root()}/REPORT/app-report.xlsx")


def test_verify_external_urls(mocker):
    mocker.patch('PACKAGES.url_verification.convert_to_csv')
    mocker.patch('PACKAGES.url_verification.lookup_dns')
    mocker.patch('PACKAGES.url_verification.dns_clean')
    mocker.patch('PACKAGES.url_verification.url_convert')
    mocker.patch('PACKAGES.url_verification.format_report')
    mocker.patch('PACKAGES.url_verification.generate_report')
    
    verify_urls('external')
    
    assert os.path.exists(f"{app_root()}/REPORT/app-report.xlsx")


def test_invalid_zone():
    with pytest.raises(ValueError):
        verify_urls('invalid')


def test_missing_files(mocker):
    mocker.patch('PACKAGES.url_verification.convert_to_csv')
    mocker.patch('PACKAGES.url_verification.err_file', side_effect=FileNotFoundError)
    
    with pytest.raises(FileNotFoundError):
        verify_urls('internal')
