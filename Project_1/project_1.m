n=20;
[x,t]=func1(n);
outputs=[]
%output=func2(x, n); % return y[n]
for i=1:20
    outputs(i)=func2(x, i); % see all y[n] from n=1 to n=20
end

[x2, t2]=func3(100) % plot range of x from -10 to 100

% use matlab filter
B=[1, 0.5]
A=[1, -1.8*cos(3.14/16), 0.81]
filter_output=filter(B, A, x2);

scatter(t, x); % plot for question 1 
scatter(t, outputs); % response from difference equation
scatter(t2, filter_output); % response from filter function

%generate x from 0 to 20
function [signal,timestamp]=func1(n) 
    signal=[]
    timestamp=[];
    if n<1
        return
    end
    
    if n>20
        return
    end
    
    for i=1:n
        if i==0
            temp=0
            signal=[signal temp]
            timestamp=[timestamp i]
        else
            temp=(0.9)^i
            signal=[signal temp]
            timestamp=[timestamp i]
        end
    end
end

% use resursion to calculate y[n]
function y=func2(x, n)
    fprintf(' n= %d ' ,n)
    
    if n<2
        fprintf(' n<2 ');        
        y=0;
    else
        fprintf(' x(n)=%d ',x(n) )
        fprintf('  in resursion  \n') 
        y=1.8.*cos(3.14/16).*func2(x, n-1)-0.81.*func2(x, n-2)+x(n)+0.5.*x(n-1);
    end
end

% generate x from -10 to 100
function [signal,timestamp]=func3(n) 
    signal=[]
    timestamp=[];
    
    for i=-10:n
        if i<0
            temp=0
            signal=[signal temp]
            timestamp=[timestamp i]
        elseif i>100
            return
        else
        temp=(0.9)^i
        signal=[signal temp]
        timestamp=[timestamp i]
        end
    end
end
