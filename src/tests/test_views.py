from django import urls
import pytest


@pytest.mark.parametrize('param', [
    'index',
    'login',
    'register',
    'error404',
    'error500',
])
def test_render_views(client, param):
    view_url = urls.reverse(param)
    resp = client.get(view_url)
    assert resp.status_code == 200


# def test_render_index(client):
#     home_url = urls.reverse('index')
#     resp = client.get(home_url)
#     assert resp.status_code == 302


def test_render_logout(client):
    logout_url = urls.reverse('logout')
    response = client.get(logout_url)
    assert response.status_code == 302
    assert response.url == urls.reverse('index')
