#!/bin/bash

set -e

echo "Creating MongoDB user and database..."

# Wait for MongoDB to start
sleep 10

# Variables
MONGO_INITDB_DATABASE="moonshot"
MONGO_INITDB_ROOT_USERNAME="moonshot"
MONGO_INITDB_ROOT_PASSWORD="moonshot"
MONGO_USER="moonshot"
MONGO_PASSWORD="moonshot"

# Create admin user
mongo moonshot -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD <<EOF
db.createUser({
  user: "$MONGO_USER",
  pwd: "$MONGO_PASSWORD",
  roles: [{ role: "readWrite", db: "$MONGO_INITDB_DATABASE" }]
})
EOF

echo "MongoDB user and database created."
