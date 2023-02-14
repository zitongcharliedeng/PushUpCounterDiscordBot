migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("zzio540hdaviyif");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "zzio540hdaviyif",
    "created": "2023-02-13 01:05:59.806Z",
    "updated": "2023-02-14 21:26:32.688Z",
    "name": "contributions",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "gyg291zc",
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
        "id": "2bf83pph",
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
})
