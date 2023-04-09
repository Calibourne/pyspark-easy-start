#!/bin/bash
docker-compose up -d
docker-compose exec work-env python examples/python/sql.py
