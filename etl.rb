require 'mongo'
require 'json'
require 'pp'

client = Mongo::Client.new([ 'ds147777.mlab.com:47777' ], :database => 'tripper', user: 'showntop', password: 'xrt310214@tz')

ch = {}
client[:categories].find().each{|c| ch[c['name']] = c['_id'] }
pp ch

ah = {}
client[:albums].find().each{|c| ah[c['name']] = c['_id'] }
pp ah


ct_array = []
at_array = []
pt_array = []
File.readlines('./items.json').each do |line|
	item = JSON.parse(line)
	ct = item['category']
	ct = '无分类' if ct == nil
	if !ch.keys.include?(ct)
		ch[ct] = ch.values.size + 1
		ct_array << {"_id": ch.values.size, "name": ct}
	end

        at = item['album']
	at = '默认' if at == nil
	if !ah.keys.include?(at)
                the_id = BSON::ObjectId.new
		ah[at] = the_id
                at_array << {"_id": the_id, "name": at}
	end

	if item['title'] == nil || item['content'] == ""
		next
	end
	ob = { :title => item['title'], category: ch[ct], asset: item['image_urls'].fetch(0, nil), content: item['content'], album:{'id': ah[at].to_s, 'name': at } }
	pt_array << ob
    # client[:projects].insert_one(ob )
end

#client[:categories].insert_many(ct_array)
ct_array.each {|ob| client[:categories].insert_one(ob) }
#client[:projects].insert_many(pt_array)
pt_array.each {|ob| client[:projects].insert_one(ob)}
at_array.each {|ob| client[:albums].insert_one(ob)}
#client[:albums].insert_many(at_array)
# pp ct_array
# pp pt_array
# pp at_array

