import random
from datetime import datetime, timedelta  
class DocumentCollaborationPlatform:
    def __init__(self):
        self.docs = {}
        self.users = {}

    def generate_random_doc_id(self):
        return str(random.randint(1000, 9999))

    def create_document(self, user_id, content=''):
        doc_id = self.generate_random_doc_id()
        if doc_id in self.docs:
            print(doc_id, "Document already exists ")
        else:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.docs[doc_id] = {'content': content, 'changes': [], 'created_at': current_datetime}
            self.users[user_id] = {'edited_docs': [doc_id]}
            print(doc_id, "Document created by", user_id, "at", current_datetime)

    def read_document(self, doc_id):
        if doc_id in self.docs:
            return self.docs[doc_id]['content']
        else:
            return None

    def update_document(self, doc_id, user_id, changes):
        if doc_id in self.docs:
            current_datetime = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.docs[doc_id]['content'] += changes
            self.docs[doc_id]['changes'].append({'user_id': user_id, 'changes': changes, 'timestamp': current_datetime})
            self.users[user_id] = {'edited_docs': [doc_id]}
            return True
        else:
            return False

    def track_changes(self, doc_id):
        if doc_id in self.docs:
            return self.docs[doc_id]['changes']
        else:
            return None

    def merge_changes(self, doc_id):
        if doc_id in self.docs:
            x = self.read_document(doc_id)
            return True
        else:
            return False

    def delete_document(self, doc_id):
        if doc_id in self.docs:
            del self.docs[doc_id]
            for user_id, user_info in self.users.items():
                if doc_id in user_info['edited_docs']:
                    user_info['edited_docs'].remove(doc_id)
            return True
        else:
            return False



dcp = DocumentCollaborationPlatform()

while True:
    print("\n1. Create document\n2. Read from document\n3. Update document\n4. Track changes\n5. Merge changes\n6. Delete document\n7. Exit")
    ch = int(input("Enter your choice:"))

    if ch == 1:
        user_id = input("Enter user ID:")
        con = input("Enter content:")
        dcp.create_document(user_id, con)

    elif ch == 2:
        doc_id = input("Enter document ID:")
        content = dcp.read_document(doc_id)
        print(f"Document content:\n{content}")

    elif ch == 3:
        doc_id = input("Enter document ID:")
        user_id = input("Enter user ID: ")
        changes = input("Enter changes: ")
        if dcp.update_document(doc_id, user_id, changes):
            print(f"Changes updated for document '{doc_id}' by user '{user_id}'.")
        else:
            print(f"Document '{doc_id}' or user '{user_id}' not found.")

    elif ch == 4:
        doc_id = input("Enter document ID:")
        changes = dcp.track_changes(doc_id)
        if changes is not None:
            print("Changes tracked:")
            for change in changes:
                print(f"User '{change['user_id']}': {change['changes']} at {change['timestamp']}")
        else:
            print(f"Document '{doc_id}' not found.")
    
    elif ch == 5:
        doc_id = input("Enter document ID:")
        if dcp.merge_changes(doc_id):
            print(f"Changes merged for document '{doc_id}'.")
            content = dcp.read_document(doc_id)
            print(f"Merge content:\n{content}")
        else:
            print(f"Document '{doc_id}' not found.")

    elif ch == 6:
        doc_id = input("Enter document ID:")
        if dcp.delete_document(doc_id):
            print(f"Document '{doc_id}' deleted.")
        else:
            print(f"Document '{doc_id}' not found.")

    elif ch == 7:
        break
