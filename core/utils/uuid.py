from multiprocessing.sharedctypes import Value
import uuid as UUID
import utils.type_validation as it

def uuid_v1():
    return UUID.uuid1()

def uuid_v3( domain ):
    assert_domain( domain )
    return UUID.uuid3( UUID.NAMESPACE_DNS, domain )

def uuid_v4():
    return UUID.uuid4()

def uuid_v5( domain ):
    assert_domain( domain )
    return UUID.uuid5( UUID.NAMESPACE_DNS, domain )

def to_uuid( val ):
    if not ( it.is_str( val ) ):
        raise ValueError( "val must be a parasable string for the uuid module to parse it correctly" )
    return UUID.UUID( val )




def assert_domain( val ):
    if val == None or it.is_str( val ):
        raise ValueError( "domain must be a non-empty string" )