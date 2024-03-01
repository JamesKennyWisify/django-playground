class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'playground':
            if model._meta.model_name in ['medicaluser', 'address']:
                return 'db_2'
            elif model._meta.model_name in ['appointment', 'entity']:
                return 'db_1'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'playground':
            if model._meta.model_name in ['medicaluser', 'address']:
                return 'db_2'
            elif model._meta.model_name in ['appointment', 'entity']:
                return 'db_1'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both models are from the same app
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow all models to be migrated to 'default' database
        if db == 'db_1':
            return True
        # Prevent 'user' and 'address' models from being migrated to 'default' database
        if app_label == 'playground' and model_name in ['medicaluser', 'address']:
            return False
        return None

    
class DjangoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions']:  
            return 'db_1'
        else:
            print(model._meta.app_label)
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in ['auth', 'admin', 'contenttypes', 'sessions']:
            return 'db_1'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # Allow relations if both models are from the same app
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # Allow all models to be migrated to non-db_1 databases
        if db != 'db_1':
            return True
        return None