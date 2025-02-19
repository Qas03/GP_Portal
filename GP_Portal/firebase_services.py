from firebase_admin import firestore

db = firestore.client()

def create_document(collection_name, document_id, data):
    ### Collection_name - firestore collection name
    ### document_id - unique id for the document
    ### data - data to store in the document

    try:
        db.collection(collection_name).document(document_id).set(data)
        print(f"Document {document_id} created/updaed in {collection_name} collection.")
    except Exception as e:
        print(f"Error in creating document: {e}")


def get_document(collection_name, document_id):
    ## Collects ducoment from firestore by document_id.

    try:
      doc = db.collection(collection_name).document(document_id).get()
      if doc.exists:
          return doc.to_dict()
      else:
          print(f"Document {document_id} not found in {collection_name} collection.")
          return None
    except Exception as e:
        print(f"Error in retrieving document: {e}")
        return None
    
def update_document(collection_name, document_id, data):
        ## Updates document in firestore by document_id. 
        try:
            db.collection(collection_name).document(document_id).update(data)
            print(f"Document {document_id} updated in {collection_name} collection.")
        except Exception as e:
            print(f"Error in updating document: {e}")

def delete_document(collection_name, document_id):
    ## Deletes document from firestore by document_id.
    try:
        db.collection(collection_name).document(document_id).delete()
        print(f"Document {document_id} deleted from {collection_name} collection.")
    except Exception as e:
        print(f"Error in deleting document: {e}")

def query_collection(collection_name, filters=None):
## Queries all documents from a collection with optional filters

    try:
        collection_ref = db.collection(collection_name)
        if filters:
            for field, op, value in filters:
                collection_ref = collection_ref.where(field, op, value)
        results = [doc.to_dict() for doc in collection_ref.stream()]
        print(f"Documents retrieved from {collection_name} collection.")
        return results
    except Exception as e:
        print(f"Error in querying collection: {e}")
        return None
    
def upload_file_to_storage(file, file_path):
    """
    Upload a file to Firebase Storage.

    Args:
        file: The file object (from Django request.FILES).
        file_path (str): The path in the Firebase Storage bucket.

    Returns:
        str: The public URL of the uploaded file.
    """
    try:
        bucket = storage.bucket()
        blob = bucket.blob(file_path)
        blob.upload_from_file(file)  # Upload file to Firebase Storage
        blob.make_public()  # Make the file publicly accessible
        print(f"File uploaded to {file_path}.")
        return blob.public_url  # Return the public URL of the file
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None