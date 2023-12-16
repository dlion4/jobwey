from tokens.models import TinyMceApiKey


def site_constants(request):
    return dict(

        # socials

        dribbble="jobwey",
        linkedin="jobwey",
        facebook="jobwey",
        instagram="jobwey",
        twitter="jobwey",

        # tinymce key

        tinymce_apikey=TinyMceApiKey.objects.filter(is_active=True).last()
        
    )