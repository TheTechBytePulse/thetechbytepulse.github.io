+++
date = '2025-07-06T14:12:25Z'
draft = false
title = 'My Lovable AI Post'
+++

Here's the detailed prompt for creating web application for AirDeals to find cheap flights between the points.

```
# Project Specification: AirDeals Flight Search Web Application

## Overview
Create a comprehensive flight search web application called "AirDeals" with the following specifications:

Build a modern, responsive flight booking platform using React, TypeScript, Tailwind CSS, and Supabase with these core features:

## Core Features

### Authentication & User Management
- Implement complete user authentication system with Supabase Auth
- User registration, login, logout functionality
- Protected routes requiring authentication
- User profile management with email and full name
- Secure session handling with JWT tokens

### Flight Search System
- Advanced flight search form with origin/destination autocomplete
- Support for round-trip and one-way flights
- Date picker integration for departure/return dates
- Passenger count and travel class selection (Economy, Premium Economy, Business, First)
- Multi-currency support (USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, KRW, SGD, HKD, AED)
- Location autocomplete with comprehensive airport database
- Real-time flight search using Amadeus API integration

### Flight Results & Display
- Professional flight results layout with airline information
- Flight duration, stops, departure/arrival times
- Dynamic pricing in user-selected currency
- Aircraft type and amenities display
- Loading states and empty states
- Responsive card-based design with hover effects

### Backend Integration
- Supabase Edge Function for flight search API calls
- Amadeus Travel API integration for real-time flight data
- Secure API key management through environment variables
- CORS-enabled API endpoints
- Error handling and logging

### User Interface
- Modern gradient hero section with branding
- Tabbed interface for Search Results, Price Alerts, and Price Trends
- Responsive design optimized for desktop and mobile
- Professional color scheme with blue/purple gradients
- Interactive components using Shadcn/UI
- Loading animations and skeleton screens

### Security Features
- Row Level Security (RLS) policies
- Secure authentication flow
- OTP expiry set to 5 minutes
- Password protection enabled
- Input validation and sanitization
- Protected API endpoints

## Technical Architecture
- React 18 with TypeScript
- Vite build system
- Tailwind CSS for styling
- Supabase for backend services
- React Router for navigation
- Date-fns for date handling
- Lucide React for icons

## Design Requirements
The application should have:
- Professional, airline-industry appearance
- Intuitive UX
- Comprehensive error handling
- Production-ready security configurations
```