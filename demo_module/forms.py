"""
This file defines form control elements for the demo_module
See: https://docs.djangoproject.com/en/2.2/topics/forms/
And: https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html

Consider validation for the JSON
https://stackoverflow.com/questions/44085153/how-to-validate-a-json-object-in-django

"""

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

#from videostream.config.localhost_dev_config import SERVER_NAME
from .models import Status


class TestForm(forms.Form):
    #         "protocolVersion": {"type": "number"},
    #         "sentBy": {"type": "string"},
    #         "msgType": {"type": "string"},
    #         "commandList": {"type": "string"},
    #         "statusCode": {"type": "string"},
    #         "parameterObj": {"type": "object"},
    #         "dataObj": {"type": "object"},
    #         "embeddedFileFormat": {"type": "string"},
    #         "embeddedFile": {"type": "string"}

    SENSOR_ID = (
        ('1', 'adxl345'),
        ('2', 'Kx224'),
    )

    SENSOR_TYPES = (
        ('1', 'SPI'),
        ('2', 'I2C'),
        ('3', 'Analog'),
    )

    START_FREQ = (
        ('100', '100 Hz'),
        ('110', '110 Hz'),
        ('120', '120 Hz'),
        ('130', '130 Hz'),
        ('140', '140 Hz'),
        ('150', '150 Hz'),
        ('160', '160 Hz'),
        ('170', '170 Hz'),
        ('180', '180 Hz'),
        ('190', '190 Hz'),
        ('200', '200 Hz'),
    )

    STOP_FREQ = (
        ('200', '200 Hz'),
    )

    STEP_FREQ = (
        ('10', '10 Hz'),
        ('50', '50 Hz'),
        ('100', '100 Hz'),
    )

    STEP_TIME_MS = (
        ('1000', '1 sek'),
    )

    sensorID = forms.ChoiceField(
        label='Type af sensor',
        choices=SENSOR_ID
    )

    sensorType = forms.CharField(
        label='Type af kommunikation',
        widget=forms.TextInput(attrs={
            'value': '1'
        }),
    )

    startFrequency = forms.ChoiceField(
        label='Test frekvens [Hz]',
        choices=START_FREQ
    )

    stopFrequency = forms.CharField(
        label='Stop frekvens',
        widget=forms.TextInput(attrs={
            'value': '0'
        }),
    )

    stepFrequency = forms.CharField(
        label='Step i Hz',
        widget=forms.TextInput(attrs={
            'value': '1'
        }),
    )

    stepTime = forms.CharField(
        label='Tid per step',
        widget=forms.TextInput(attrs={
            'value': '1'
        }),
    )

    # Who requested this data
    sender = forms.CharField(
        label='Opretter (navn)',
        required=True,
        widget=forms.TextInput(attrs={
            'value': 'testbruger'
        })
    )

    # tag data to keep it in the db forever
    no_delete = forms.BooleanField(
        label='Gem data permanent',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(

            Row(
                Column('sensorID', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('startFrequency', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'sender',
            'no_delete',
            Submit('submit', 'Start test')
        )


class AccelerometerForm(forms.Form):
    """
    Denne klasse implementerer formularen til GUI-demo, som vises på Webinterface
    """
    SENSOR_TYPES = (
        ('adxl345', 'adxl345'),
        ('Kx224', 'Kx224'),
    )

    FREQ_LIST = (
        ('10', '10 Hz'),
        ('100', '100 Hz'),
        ('1000', '1 kHz'),
        ('10000', '10 kHz'),
    )

    sensor_type = forms.ChoiceField(
        label='Sensortype',
        choices=SENSOR_TYPES
    )

    duration = forms.CharField(
        label='Varighed af test (sekunder)',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast antal sekunder her'
        }),
        required=True
    )

    step = forms.CharField(
        label='Steps',
        widget=forms.TextInput(attrs={
            'placeholder': 'Indtast steps her'
        }),
        required=True
    )

    stepTime = forms.CharField(
        label='Steptime i [ms]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepTime her'
        }),
        required=True
    )

    stepSize = forms.CharField(
        label='Steptime [int]',
        widget=forms.TextInput(attrs={
            'value': '10',
            'placeholder': 'Indtast stepSize her'
        }),
        required=True
    )

    freq = forms.ChoiceField(
        label='Frekvens [Hz]',
        choices=FREQ_LIST
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'sensor_type',
            'duration',
            'step',
            'stepTime',
            'stepSize',
            'freq',
            Submit('submit', 'En knap :)')
        )