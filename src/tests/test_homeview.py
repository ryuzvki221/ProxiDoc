from django import urls




def test_render_views(client):
   home_url = urls.reverse('index')
   resp = client.get(home_url)
   assert resp.status_code == 302