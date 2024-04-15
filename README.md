# Graphql Federation test
Command line to laubch the apps:
```
cd books && strawberry server --port 3500 app
cd reviews && strawberry server --port 3000 app
```

Command line to generate schema for supergraph:
```
rover supergraph compose --config ./supergraph.yaml --skip-update --elv2-license accept --output supergraph.graphql
```

Command line to launch Apollo router with federation:
```
./router --supergraph supergraph.graphql --log trace
```