from httpx import AsyncClient

async def test_get_professions(client: AsyncClient):
    """
    Test para obtener la lista de profesiones.
    Verifica que la respuesta es exitosa y contiene los datos esperados.
    """
    response = await client.get("/api/v1/professions")
    
    assert response.status_code == 200
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0 # Asumimos que las migraciones insertan al menos una profesión
    assert "name" in data[0]
    assert "description" in data[0]
    assert "base_stats" in data[0]
    assert "base_inventory" in data[0]