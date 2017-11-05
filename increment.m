function [index,force] = increment(t,x)
v1=0;
L=100;
dt=0.001;
V_amp=200;%in mV
a=0.3;
v2_u = 1:V_amp/(a*L):V_amp;
v2_d = V_amp - V_amp/(L*(1-a)):-(V_amp/(L*(1-a))):0;
v2 = [v2_u,v2_d];
v2_t = [v2,v2,v2,v2,v2,v2,v2,v2,v2,v2];
plot(v2_t);
T = 1;
t_on = 0.8*T;
t_off = T - t_on;
kT = 26;
if (t*dt - floor(t*dt)) <= t_on 
    v = V_amp/kT;
    if mod(x,100) < a*L
        disp('mod');
        disp(mod(x,100));
        disp('x');
        disp(x);
        force = -v/a;
    else
        force = v/(1-a);
    end
        disp('force');
    disp(force);
    index=1;
else
    force = 0;
    index = 0;
end
