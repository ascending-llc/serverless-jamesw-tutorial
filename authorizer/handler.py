import requests
from jose import jwk, jwt
from pprint import pprint
from jose.utils import base64url_decode
import os

def lambda_handler(event, context):
    token = event['authorizationToken']
    UserPoolId=os.environ['USER_POOL_ID']
    
    # Decode the headers and payload without verifying signature
    access_headers = jwt.get_unverified_header(token)
    access_claims = jwt.get_unverified_claims(token)

    # Retrieves JSON Web Key Set, which contains two public keys
    jwks_url = f'https://cognito-idp.us-west-1.amazonaws.com/{UserPoolId}/' \
                '.well-known/jwks.json'
    r = requests.get(jwks_url)
    if r.status_code == 200:
        jwks = r.json()
    else:
        raise 'Did not retrieve JWKS, got {}'.format(str(r.status_code))
        
    kid = access_headers['kid']
    # get the public key that corresponds to the key id from headers
    key_index = -1
    for i in range(len(jwks['keys'])):
        if kid == jwks['keys'][i]['kid']:
            key_index = i
            break
    if key_index == -1:
        print('Public key not found, can not verify token')
    else:
        # convert public key to the proper format
        public_key = jwk.construct(jwks['keys'][key_index])
        # get claims and signature from token
        claims, encoded_signature = token.rsplit('.', 1)
        # decrypted signature must match header and payload
        decoded_signature = base64url_decode(
                                encoded_signature.encode('utf-8'))
        if not public_key.verify(claims.encode("utf8"),
                                 decoded_signature):
            print('Signature verification failed')
        else:
            print('Signature successfully verified')
            
            return generatePolicy('apiCaller','Allow', event['methodArn'])


def generatePolicy(principalId, effect, methodArn):
    authResponse = {}
    authResponse['principalId'] = principalId

    if effect and methodArn:
        policyDocument = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': methodArn
                }
            ]
        }

        authResponse['policyDocument'] = policyDocument

    return authResponse            