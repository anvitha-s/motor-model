%force exterted on motor due to potential field
function [index,force] = increment(t,x)
%flat potential v1
v1_t=0;
%time step
dt=0.001;
%amplitude of sawtooth
V_amp=200;
%fraction of sawtooth with positive slope
a=0.3;
%length of one sawtooth field in x
L=100;
%generating sawtooth potential field v2_t
v2_u = 1:V_amp/(a*L):V_amp;
v2_d = V_amp - V_amp/(L*(1-a)):-(V_amp/(L*(1-a))):0;
v2 = [v2_u,v2_d];
v2_t = [v2,v2,v2,v2,v2,v2,v2,v2,v2,v2];
plot(v2_t);
%time period of cycle of swithching
T = 1;
%time for which sawtooth potential is switched on
t_on = 0.8*T;
t_off = T - t_on;
% kT - boltzmann constant*temperature(300K) 
kT = 26;
if (t*dt - floor(t*dt)) <= t_on 
    %sawtooth potential is on
    v = V_amp/kT;
    if mod(x,100) < a*L
        %upward slope of sawtooth potential
        disp('mod');
        disp(mod(x,100));
        disp('x');
        disp(x);
        force = -v/a;
    else
        %downward slope of sawtooth potential
        force = v/(1-a);
    end
        disp('force');
    disp(force);
    %index denotes v2 is on
    index=1;
else
    force = 0;
    %index denotes v1 is on
    index = 0;
end