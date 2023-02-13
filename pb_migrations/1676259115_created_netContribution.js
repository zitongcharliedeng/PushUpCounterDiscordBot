migrate((db) => {
  const collection = new Collection({
    "id": "io58nniitequ5oc",
    "created": "2023-02-13 03:31:55.792Z",
    "updated": "2023-02-13 03:31:55.792Z",
    "name": "netContribution",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "p3kwjt8x",
        "name": "userId",
        "type": "text",
        "required": false,
        "unique": true,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "qaegffja",
        "name": "pushups",
        "type": "number",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null
        }
      }
    ],
    "listRule": "",
    "viewRule": "",
    "createRule": "",
    "updateRule": "",
    "deleteRule": "",
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("io58nniitequ5oc");

  return dao.deleteCollection(collection);
})
