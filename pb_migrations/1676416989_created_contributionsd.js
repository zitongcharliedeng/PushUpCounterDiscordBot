migrate((db) => {
  const collection = new Collection({
    "id": "u6y1r381qcg6kc6",
    "created": "2023-02-14 23:23:09.032Z",
    "updated": "2023-02-14 23:23:09.032Z",
    "name": "contributionsd",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "ifkciuhn",
        "name": "userId",
        "type": "text",
        "required": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "uf64wes3",
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
  const collection = dao.findCollectionByNameOrId("u6y1r381qcg6kc6");

  return dao.deleteCollection(collection);
})
