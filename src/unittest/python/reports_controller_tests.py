'''
Created on 03-Nov-2017

@author: karthikeyan
'''
import unittest
from flask import Flask
from mock import patch
from com.jeavio.controller import reports_controller
from com.jeavio.service.report_service import ReportService

app = reports_controller.app   

class ControllerTest(unittest.TestCase):

    app = app.test_client()
    app.testing = True
    controller = reports_controller
    
    @patch.object(ReportService, "get_all_cpu_report")
    def test_get_cpu_report(self, mock_cpu_report):
        result = self.app.get('/report/cpu')
        self.assertEqual(result.status_code, 200)
    
    @patch.object(ReportService, "get_all_ram_report")
    def test_get_virtual_memory_report(self, mock_ram_report):
        result = self.app.get('/report/virtualmemory')
        self.assertEqual(result.status_code, 200)
    
    @patch.object(Flask, "run")
    def test_start_flask(self, mock_run):
        self.controller.start_flask()
        self.assertTrue(mock_run.called)
        
        