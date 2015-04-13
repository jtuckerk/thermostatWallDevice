//
//  ViewController.swift
//  SimpleThermostat
//
//  Created by Tucker Kirven on 1/30/15.
//  Copyright (c) 2015 Tucker Kirven. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
 /*
    var home1 = Home()
  
    var socketQueue:dispatch_queue_t!
    var listenSocket:GCDAsyncSocket!
    var connectedSockets:NSMutableArray!
    
        @IBAction func switch2Schedule(sender: AnyObject) {
     
        
    }

    @IBAction func upButton(sender: AnyObject) {
        home1.increaseSetPoint()
        setPointTextField.text = toString(home1.setPoint)
        sendSetPoint()
        
    }
    @IBAction func downButton(sender: AnyObject) {
        home1.decreaseSetPoint()
        setPointTextField.text = toString(home1.setPoint)
        sendSetPoint()
    }
    @IBOutlet weak var message: UILabel!
    
    func sendSetPoint(){
        var msg:String = toString(home1.setPoint)
        var msgData:NSData = msg.dataUsingEncoding(NSUTF8StringEncoding)!
        var sock:GCDAsyncSocket
        
        message.text = ("writing \(msg) to \(socket) \n")
        for socket in connectedSockets
        {
            message.text = ("writing \(msg) to \(toString(socket)) \n")
            socket.writeData(msgData, withTimeout: 1, tag: 0) //need to add timeout and tag?
            
        }
    }

    @IBOutlet weak var setPointTextField: UILabel!

    @IBOutlet weak var tempTextField: UILabel!
   
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        //setPointTextField.text = toString(home1.setPoint)
        //tempTextField.text = toString(home1.temp)
        
        
        //socketQueue = dispatch_queue_create("socketQueue", nil)
        
        //listenSocket = GCDAsyncSocket(delegate:self, delegateQueue:socketQueue)
        
        //connectedSockets = NSMutableArray(capacity: 1)
        
        
        
        var port:UInt16 = 2345;
        var err:NSError?
       /*
        while(!listenSocket.acceptOnPort(port, error: &err))
        {
            message.text = "not connected"
           NSLog("error starting server ");
           return;
        }
        */
    }
    func socket(sock: GCDAsyncSocket!, didAcceptNewSocket newSocket:GCDAsyncSocket!){
    // This method is executed on the socketQueue (not the main thread)
    
        synced(connectedSockets)
        {
            self.connectedSockets.addObject(newSocket);
            self.message.text = "added socket to list"

        }
        var host:String = newSocket.connectedHost
        
        var port: UInt16 = newSocket.connectedPort
    
        NSLog("Accepted client %@:%hu", host, port);
    
    }

    func socketDidDisconnect(sock: GCDAsyncSocket!, withError err:NSError!)
    {
        if (sock != listenSocket)
        {
            ("client disconnected");
    
            synced(connectedSockets)
            {
                self.connectedSockets.removeObject(sock)
            }
        }
    }

    func synced(lock: AnyObject, closure: () -> ()) {
        objc_sync_enter(lock)
        closure()
        objc_sync_exit(lock)
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }



*/
}
