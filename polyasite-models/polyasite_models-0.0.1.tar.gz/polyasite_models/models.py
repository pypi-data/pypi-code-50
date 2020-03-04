from mongoengine import Document, EmbeddedDocument, QuerySet, StringField, IntField, EmbeddedDocumentField, FloatField, BooleanField, ListField, LazyReferenceField
import logging

logger = logging.getLogger(__name__)

#################################
# Define classes for MongoDB
# Author: christina.herrmann@unibas.ch
# Created: 20191210
#
# These class definitions determine the MongoDB schema
# for the polyasite database. To be used in cjh-results-into-db-NEW.py
# Use the same classes for the polyapp (specify in models.py)
# to ensure consistency and schema validation.
#################################

############################
# Custom query set manager #
############################
class ValidQuerySet(QuerySet):
    
    def valid_objects(self, verbose=False):
        '''
        Before returning results from database, check whether all objects
        of the query comply with the currently defined classes. Return a queryset that only contains compliant objects.
        If this test is ommitted, individual views will crash if one of 
        their serving documents contains undefined fields, or, if meta={'strict':False} is set, views will render with valid objects but logging for invalid objects is not possible and errors in schemas are hard to track.
        Usage: CLASSNAME.objects.valid_objects()
                add meta = {'queryset_class': ValidQuerySet} to Class definition
        '''
        cnt = self.count()
        
        # Collect ids of valid objects
        wanted = []
        # Collect list of error messages
        errors = []

        # Make sure we try for all objects; without the while loop the function will exit as soon as one invalid object has been identified and further valid objects will be missed.
        while cnt:
            try:
                if len(set(wanted)) == cnt:
                        # We found all valid objects, finished
                        break
                for q in self:
                    # As long as objects are valid, append their id
                    wanted.append(q.pk)
                    
            except Exception as e:
                # Encountered an invalid object
                errors.append(e)
                # Valid objects minus 1, then try iterating again!
                cnt -= 1

        q_set = self(pk__in=set(wanted))
        
        if errors and verbose:
            
            logger.critical("\tSome documents in your database do not comply with the defined class schema.")
            logger.critical("\tThe content of these documents will not be accessed.")
            logger.critical("\tCheck error message below and adapt the schema or the documents accordingly.")
            
            if len(errors)>10:
                logger.critical("{} invalid documents, only displaying first 10 messages.".format(len(errors)))
                for error in errors[0:10]:
                    logger.critical(error)
            else:
                for error in errors:
                    logger.critical(error)
             
        return q_set

    def invalid_set(self):
        '''
        Get a list of invalid objects, by comparing pks for all objects in the database with the result of the valid_objects method.
        Also give warning when there are no results, this most likely means that the queried collection doesn't exist.
        '''
        all_documents = [str(x) for x in self.distinct("_id")]
        if not all_documents:
            logger.critical("\tNo documents have been found. Make sure that the collections you are querying exist in the database.")
            
        valid_documents = [str(x) for x in self.valid_objects(verbose=True).distinct("_id")]
        invalid_set = set(all_documents).difference(set(valid_documents))

        return invalid_set



######################
# Samples collection #
######################


class Strand(EmbeddedDocument):
    plus = IntField(required=True)
    minus = IntField(required=True)

class Reads(EmbeddedDocument):
    trimmed = IntField(required=True)
    multimappers = IntField(required=True)
    uniquemappers = IntField(required=True)
    valid = IntField(required=True)
    PAsites = EmbeddedDocumentField(Strand)
    IP = EmbeddedDocumentField(Strand)
    noBG = IntField(required=True)
    noBG_PAS = IntField(required=True) 
    


class Sample_Sites(EmbeddedDocument):
    PAsites = EmbeddedDocumentField(Strand)
    IP = EmbeddedDocumentField(Strand)
    noBG = IntField(required=True)
    noBG_PAS = IntField(required=True)
    


class Version(EmbeddedDocument):

    version_name = StringField(max_length=10, required=True)
    description = StringField(max_length=1000)
    releaseDate = StringField(max_length=20)
    genome = StringField(max_length=20, required=True)
    ucsc_db = StringField(max_length=4, required=True)
    valid_max_len = IntField(required=True)
    valid_max_As = FloatField(required=True)
    valid_max_Ns = IntField(required=True)
    reads = EmbeddedDocumentField(Reads)
    sites = EmbeddedDocumentField(Sample_Sites)



class Samples(Document):
    '''Using sampleID as primary key to ensure 
    uniqueness of entries'''
    sampleID = StringField(max_length=20, primary_key=True)
    seriesID = StringField(max_length=20, required=True)
    title = StringField(max_length=200)
    PubMedID = StringField(required=True)
    protocol = StringField(max_length=50, required=True)
    organism = StringField(max_length=50, required=True)
    source = StringField(max_length=200)
    treatment = StringField(max_length=200)
    sex = StringField(choices=( 'NA', 'M', 'F'))
    visible = BooleanField(default=True)
    raw_read_count =IntField(required=True)
    raw_max_len = IntField(required=True)
    raw_min_len = IntField(required=True)
    versions = ListField(EmbeddedDocumentField(Version))

    meta = {
        'queryset_class': ValidQuerySet
        }



######################
# Atlas collection #
######################

class Clusters(EmbeddedDocument):
    primary = IntField(required=True)
    merged = IntField(required=True)
    PAS = IntField(required=True)
    TE = IntField(required=True)
    EX = IntField(required=True)
    IN = IntField(required=True)
    DS = IntField(required=True)
    IG = IntField(required=True)
    AI = IntField(required=True)
    AE = IntField(required=True)
    AU = IntField(required=True)
    


class Atlas_Sites(EmbeddedDocument):
    pooled = IntField(required=True)
    noBG = IntField(required=True)



class Atlas(Document):
    '''Use a combination of genome and atlas version as pk
    Note: Not using DateTimeField for releaseDate because the timestamp that was created by to_json upon data retrival was not valid.
    '''
    AtlasID = StringField(max_length=20, primary_key=True)
    version_name = StringField(max_length=10, required=True)
    description = StringField(max_length=1000)
    genome = StringField(max_length=20, required=True)
    ucsc_db = StringField(max_length=4, required=True)
    organism = StringField(max_length=50, required=True)
    public = BooleanField(default=True)
    releaseDate = StringField(required=True)
    sampleIDs = ListField(LazyReferenceField(Samples, required=True))  # Couldn't get the reverse_delete_rule to work.
    polyAsignals = ListField(StringField(max_length=7), required=True)
    clusters = EmbeddedDocumentField(Clusters)
    sites = EmbeddedDocumentField(Atlas_Sites)
    
    meta = {
        'queryset_class': ValidQuerySet
        }

######################
# Protocols collection #
######################

class Protocols(Document):
    name = StringField(required=True, primary_key = True)
    text = StringField(required=True)
    image = StringField(required=True)

    meta = {
        'queryset_class': ValidQuerySet
        }

######################
# Publications collection #
######################

class Publications(Document):
    PubMedID = StringField(required=True, primary_key = True)
    citation = StringField(required=True)

    meta = {
        'queryset_class': ValidQuerySet
        }