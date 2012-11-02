//
//  ViewController.m
//  blendImages
//
//  Created by greentea on 12-10-30.
//  Copyright (c) 2012年 greentea. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

@synthesize imageV;
- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    UIImage *source = imageV.image;
    //NSLog(@"width:%f,height:%f",imageV.frame.size.width,imageV.frame.size.height);
    UIGraphicsBeginImageContextWithOptions(source.size, NO, source.scale);
    CGContextRef context = UIGraphicsGetCurrentContext();
    CGContextTranslateCTM(context, 0, source.size.height);
    CGContextScaleCTM(context, 1.0, -1.0);
    CGRect rect = CGRectMake(0, 0, source.size.width, source.size.height);
//    [source drawInRect:rect];
    CGContextDrawImage(context, rect, source.CGImage);
    
//    CGContextSetBlendMode(context, kCGBlendModeMultiply);
//    CGContextSetFillColorWithColor(context, [UIColor redColor].CGColor);
    [[UIColor redColor] set];
    CGContextClipToMask(context, rect, source.CGImage);
    CGContextSetAlpha(context, 0.5);
    CGContextFillRect(context, rect);
    UIImage *colorImage = UIGraphicsGetImageFromCurrentImageContext();
    UIGraphicsEndImageContext();
    imageV.image = colorImage;    
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)dealloc {
    [imageV release];
    [super dealloc];
}
- (void)viewDidUnload {
    [self setImageV:nil];
    [super viewDidUnload];
}
@end
