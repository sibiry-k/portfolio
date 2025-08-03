#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo "Запускаем тесты..."

echo "Остановка существующих контейнеров..."
docker compose -f compose.tests.yaml down -v

echo "Сборка и запуск тестовых контейнеров..."
docker compose -f compose.tests.yaml up --build --abort-on-container-exit

exit_code=$?

echo "Очистка..."
docker compose -f compose.tests.yaml down -v

if [ $exit_code -eq 0 ]; then
    echo "Все тесты прошли успешно!"
else
    echo "Тесты завершились с ошибками (код: $exit_code)"
fi

exit $exit_code
