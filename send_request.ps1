$data = Get-Content -Raw -Path "data.json"

# Выполнение POST-запроса
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/calculate" -Method Post -Body $data -ContentType "application/json"
# Печать ответа
$response


try {
    $body = @{
        "key1" = "value1"
        "key2" = "value2"
    }

    $response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/calculate" -Method Post -Body ($body | ConvertTo-Json) -ContentType "application/json"
    Write-Output "Ответ: $response"
} catch
{
    Write-Output "Ошибка: $_"
}