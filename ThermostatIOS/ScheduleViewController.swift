//
//  ScheduleViewController.swift
//  SimpleThermostat
//
//  Created by Tucker Kirven on 3/25/15.
//  Copyright (c) 2015 Tucker Kirven. All rights reserved.
//

import Foundation

import UIKit



class scheduleViewController: UIViewController {
    
    @IBAction func connect(sender: AnyObject) {
        
        appDelegate.connection!.bigSendTest()
        messageOut.text = appDelegate.connection?.status
    }
    
    @IBOutlet weak var messageOut: UILabel!
    let appDelegate = UIApplication.sharedApplication().delegate as AppDelegate
    
    @IBOutlet var view1: UIView!
    
    @IBAction func dayOfWeekSend(sender: AnyObject) {
        appDelegate.connection!.status = "here2"
        appDelegate.connection!.getSchedule()

        
        appDelegate.connection!.status = "here3"
        self.performSegueWithIdentifier("dayOfWeek", sender: sender)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        appDelegate.currVC = self

    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        
        if segue.identifier == "dayOfWeek"{
        var controller: DayScheduleViewController = segue.destinationViewController as DayScheduleViewController
        var identifier1 = segue.identifier
        NSLog("segue: " + identifier1!)
        var sender1 = sender!.currentTitle
        NSLog("sender: " + sender1!!)
        controller.day = sender1!!
        }
    }
   
}
