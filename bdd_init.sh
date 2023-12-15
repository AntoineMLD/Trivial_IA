#script permettant de créer la database vierge

db_name="Trivial_bdd.db"

sqlite3 "$db_name" <<EOF

.databases
.exit
EOF