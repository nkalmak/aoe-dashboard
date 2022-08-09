from rec_downloader.rec_download import steam_id, profile_id
import pytest

@pytest.mark.parametrize("test_input, expected", [
    (len(steam_id), 17),
    (len(profile_id), 6)
])

def test_user_data(test_input, expected):
    assert test_input is expected

# def test_rec_download():
#     assert len(steam_id) == 17, 'valid steam ID'
 