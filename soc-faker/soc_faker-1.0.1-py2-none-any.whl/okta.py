GET_ALL_APPS = '''
{
    "status": "ACTIVE", 
    "name": "oidc_client", 
    "created": "2020-02-05T21:37:06.000Z", 
    "settings": {
        "notifications": {
            "vpn": {
                "message": null, 
                "helpUrl": null, 
                "network": {
                    "connection": "DISABLED"
                }
            }
        }, 
        "app": {}, 
        "oauthClient": {
            "redirect_uris": [
                "http://localhost:8080/implicit/callback"
            ], 
            "client_uri": null, 
            "application_type": "browser", 
            "grant_types": [
                "authorization_code"
            ], 
            "post_logout_redirect_uris": [
                "http://localhost:8080"
            ], 
            "response_types": [
                "code"
            ], 
            "logo_uri": null, 
            "issuer_mode": "ORG_URL"
        }
    }, 
    "accessibility": {
        "selfService": false, 
        "errorRedirectUrl": null, 
        "loginRedirectUrl": null
    }, 
    "lastUpdated": "2020-02-05T21:37:06.000Z", 
    "label": "My SPA", 
    "_links": {
        "deactivate": {
            "href": "https://dev-547249.oktapreview.com/api/v1/apps/0oaplmazp7H6baaMS0h7/lifecycle/deactivate"
        }, 
        "logo": [
            {
                "href": "https://op1static.oktacdn.com/assets/img/logos/default.6770228fb0dab49a1695ef440a5279bb.png", 
                "type": "image/png", 
                "name": "medium"
            }
        ], 
        "appLinks": [
            {
                "href": "https://dev-547249.oktapreview.com/home/oidc_client/0oaplmazp7H6baaMS0h7/aln5z7uhkbM6y7bMy0g7", 
                "type": "text/html", 
                "name": "oidc_client_link"
            }
        ], 
        "users": {
            "href": "https://dev-547249.oktapreview.com/api/v1/apps/0oaplmazp7H6baaMS0h7/users"
        }, 
        "groups": {
            "href": "https://dev-547249.oktapreview.com/api/v1/apps/0oaplmazp7H6baaMS0h7/groups"
        }
    }, 
    "visibility": {
        "appLinks": {
            "oidc_client_link": true
        }, 
        "autoSubmitToolbar": false, 
        "hide": {
            "web": true, 
            "iOS": true
        }
    }, 
    "credentials": {
        "signing": {
            "kid": "cpgk-XHuvTDVEw82rYHOCjD1l3HcFbJgMfBvSk-L3iw"
        }, 
        "oauthClient": {
            "token_endpoint_auth_method": "none", 
            "autoKeyRotation": true, 
            "client_id": "0oaplmazp7H6baaMS0h7"
        }, 
        "userNameTemplate": {
            "type": "BUILT_IN", 
            "template": "${source.login}"
        }
    }, 
    "signOnMode": "OPENID_CONNECT", 
    "id": "0oaplmazp7H6baaMS0h7", 
    "features": []
}''''